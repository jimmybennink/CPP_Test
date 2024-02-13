#include <iostream>
#include<tuple>
#include<array>

// Needed to export functions on Windows
#ifdef _WIN32
#   define API __declspec(dllexport)
#else
#   define API
#endif


class PX4_Controllers{
    public:
        //PX4_Controllers();
        //~PX4_Controllers();

        //float pos_accel_control();
        //float att_control();
        //float rate_control();
        //float mixing();

        void run(){
            std::cout << "Running..." << std::endl;
        }

        void run_floats(float *inp1, float *inp2){
            *inp1 = *inp1 * 2;
            *inp2 = *inp2 * 3;
        }
};

extern "C" {
    API PX4_Controllers* Controller_init(){ return new PX4_Controllers(); }
    API void Run_Controller(PX4_Controllers* PX4_Controllers){ PX4_Controllers->run(); }
    API void Run_Floats(PX4_Controllers* PX4_Controllers, float* arg1, float* arg2){ return PX4_Controllers->run_floats(arg1, arg2); }
}