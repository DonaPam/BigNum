#include <cmath>
double daily_rate(double hourly_rate) {
    return hourly_rate * 8;
}
double apply_discount(double before_discount, double discount) {
    return before_discount - (before_discount * discount / 100);
}
int monthly_rate(double hourly_rate, double discount) { 
    return std::ceil(((hourly_rate * 8 * 22) - ((hourly_rate * 8 * 22) * discount/100))) ;
}
int days_in_budget(int budget, double hourly_rate, double discount) {
    return budget / (hourly_rate * 8 -(hourly_rate * 8 * discount/100 ));
}