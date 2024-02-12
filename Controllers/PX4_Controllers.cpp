#include <iostream>

class PX4_Controllers{
    public:
        void run(){
            std::cout << "Running..." << std::endl;
        }
};

extern "C" {
    PX4_Controllers* Controller_init(){ return new PX4_Controllers(); }
    void Run_Controller(PX4_Controllers* PX4_Controllers){ PX4_Controllers->run(); }
}