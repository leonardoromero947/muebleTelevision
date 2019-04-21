import com.pi4j.io.gpio.GpioController;
import com.pi4j.io.gpio.GpioFactory;
import com.pi4j.io.gpio.GpioPinDigitalInput;
import com.pi4j.io.gpio.GpioPinDigitalOutput;
import com.pi4j.io.gpio.PinPullResistance;
import com.pi4j.io.gpio.PinState;
import com.pi4j.io.gpio.RaspiPin;
import controller.GpioUsageExampleListener;

public class Start  {

    //+++++++++++++++++++++++
    //Comentario prueba
    //++++++++++++++++++++++
    public static void main (String [ ] args) {
        final GpioController gpio = GpioFactory.getInstance();

        GpioPinDigitalInput myButton = gpio.provisionDigitalInputPin(RaspiPin.GPIO_25, "MyButton", PinPullResistance.PULL_DOWN);
        GpioPinDigitalOutput myLed = gpio.provisionDigitalOutputPin(RaspiPin.GPIO_16, "My LED",PinState.LOW);  
                                                                     
        for(int x =1;x>0;x++){
            /*
            if(myButton.getState().isHigh()){
                System.out.print("Hola");
                myLed.pulse(5000);
            }
            */
            myButton.addListener(new GpioUsageExampleListener());

        }
        
    }

}
