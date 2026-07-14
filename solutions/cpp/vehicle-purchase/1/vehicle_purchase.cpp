#include "vehicle_purchase.h"
#include <iostream>
#include <string>

namespace vehicle_purchase {
bool needs_license(std::string kind) {
    bool result ;
    if ( kind == "car" || kind == "truck")
         result = true;
    else result = false ;
    return result;
}
std::string choose_vehicle(std::string option1, std::string option2) {
    std::string result;
    if (option1 <= option2)
        result = option1 + " is clearly the better choice.";
    else result = option2 + " is clearly the better choice.";
    return result;
}
double calculate_resell_price(double original_price, double age) {
    double result;
    if ( age < 3){
        result = original_price * 0.8;
    }
    else if ( age >= 10){
        result = original_price * 0.5;
    }
    else {
        result = original_price * 0.7;
    }
    
    return result;
}

}  // namespace vehicle_purchase
