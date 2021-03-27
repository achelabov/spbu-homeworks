#include <iostream>
#include <fstream>
#include <string>

int main()
{
    std::fstream fbin;
    std::string line = "The vowels in this sentence will be replaced";
/*    fbin.open("file.bin", std::ios::binary | std::ios::out);

   
    fbin.write((char*)&n, sizeof(std::string::size_type));
    fbin.write(line.c_str(), line.size());
    fbin.close(); */

    fbin.open("file.txt", std::ios::binary | std::ios::in | std::ios::out);
    std::string::size_type n = line.size();
    fbin.read((char*)&n, sizeof(std::string::size_type));
    std::string sout(n, 0);

    for (int i = 0; i < n; ++i)
    {
        fbin.read(&sout[i], sizeof(sout[0]));
    }
    std::cout << sout << std::endl;

    fbin.close();

    return EXIT_SUCCESS;
}
