#include <iostream>
#include <fstream>
#include <vector>
#include <map>

using namespace std;

int main( int argc, char** argv ){

	if( argc != 2 ){
		cerr << "Incorrect number of arguments. Please instead use:\n";
		cerr << "\t./code [degauss.EDMdat file]\n";
		return 0;
	}
	
	// Read in input file as binary
	ifstream file (argv[1], ios::binary);

	// Prep data storage
	std::map<int,std::vector<double>> full_data;
	int channel = 0;
	const double DEFAULT = -1e5;
	for (double read = DEFAULT; file.read(reinterpret_cast<char*>(&read), sizeof(read)); ){

		if( read != DEFAULT ) full_data[channel].push_back( read );

		// Only 9 outputs per time measurement
		if( channel == 9 ){
			channel = 0;
			continue;
		}
		channel++;

	}

	// Channel 1 = voltage
	// Channel 2 = current
	for( int i = 0 ; i < full_data[0].size() ; ++i){
		cout << i << " " << full_data[1][i] << " " << full_data[2][i] << "\n";
	}

	// Exit
	return 1;
}
