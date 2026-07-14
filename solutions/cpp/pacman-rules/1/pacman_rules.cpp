bool can_eat_ghost(bool power_pellet_active, bool touching_ghost) {
    bool result = power_pellet_active && touching_ghost;
    return result ;
}
bool scored(bool touching_power_pellet, bool touching_dot) {
    bool result = touching_power_pellet || touching_dot;
    return result;
}
bool lost(bool power_pellet_active, bool touching_ghost) {
    bool result = !power_pellet_active && touching_ghost;
    return result ;
}
bool won(bool has_eaten_all_dots, bool power_pellet_active,
         bool touching_ghost) {
    bool result = has_eaten_all_dots && !(!power_pellet_active && touching_ghost);
    return result;
}
