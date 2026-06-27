#include <string>
namespace log_line {
std::string message(std::string line) {
     int num = line.find(" ");
 std::string new_line = line.substr(num + 1 );
 return new_line;
}

std::string log_level(std::string line) {
    int num = line.find("]");
    std::string new_line = line.substr(1,num - 1);
    return new_line;
}

std::string reformat(std::string line) {
    // return the reformatted message
    
   std::string new_line = line.substr(line.find(":") + 2) +" (" + line.substr(1,line.find("]") - 1) + ")";
    return new_line ;
}
}  // namespace log_line
