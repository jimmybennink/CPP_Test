#include <iostream>
#include<tuple>

// Needed to export functions on Windows
#ifdef _WIN32
#   define API __declspec(dllexport)
#else
#   define API
#endif

class PX4_Controllers{
    public:
        void run(){
            std::cout << "Running..." << std::endl;
        }

        std::tuple <float, float> run_floats(float input){
            
            float two = input * 2.0;
            float three = input * 3.0;
            return std::make_tuple(two, three);
        }
};

extern "C" {
    API PX4_Controllers* Controller_init(){ return new PX4_Controllers(); }
    API void Run_Controller(PX4_Controllers* PX4_Controllers){ PX4_Controllers->run(); }
    API std::tuple <float, float> Run_Floats(PX4_Controllers* PX4_Controllers, float inp){ return PX4_Controllers->run_floats(inp); }
}