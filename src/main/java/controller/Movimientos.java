package controller;

import com.pi4j.io.gpio.GpioController;
import com.pi4j.io.gpio.GpioFactory;
import com.pi4j.io.gpio.GpioPinDigitalInput;
import com.pi4j.io.gpio.GpioPinDigitalOutput;
import com.pi4j.io.gpio.PinPullResistance;
import com.pi4j.io.gpio.PinState;
import com.pi4j.io.gpio.RaspiPin;

public class Movimientos {
    //Activacion de control del GPIO
    final GpioController gpio = GpioFactory.getInstance();

    private boolean eterno = true;
    //INSTANCIADO DE LEDS
    GpioPinDigitalOutput puenteH1L = gpio.provisionDigitalOutputPin(RaspiPin.GPIO_16, "LED1",PinState.LOW);
    GpioPinDigitalOutput puenteH1R = gpio.provisionDigitalOutputPin(RaspiPin.GPIO_01, "LED2",PinState.LOW);
    GpioPinDigitalOutput puenteH2L = gpio.provisionDigitalOutputPin(RaspiPin.GPIO_04, "LED3",PinState.LOW);
    GpioPinDigitalOutput puenteH2R = gpio.provisionDigitalOutputPin(RaspiPin.GPIO_06, "LED4",PinState.LOW);
    GpioPinDigitalOutput puenteH3L = gpio.provisionDigitalOutputPin(RaspiPin.GPIO_10, "LED5",PinState.LOW);
    GpioPinDigitalOutput puenteH3R = gpio.provisionDigitalOutputPin(RaspiPin.GPIO_11, "LED6",PinState.LOW);
    GpioPinDigitalOutput puenteH4L = gpio.provisionDigitalOutputPin(RaspiPin.GPIO_26, "LED7",PinState.LOW);
    GpioPinDigitalOutput puenteH4R = gpio.provisionDigitalOutputPin(RaspiPin.GPIO_27, "LED8",PinState.LOW);
    GpioPinDigitalOutput puenteH5L = gpio.provisionDigitalOutputPin(RaspiPin.GPIO_28, "LED9",PinState.LOW);
    GpioPinDigitalOutput puenteH5R = gpio.provisionDigitalOutputPin(RaspiPin.GPIO_29, "LED10",PinState.LOW);
    GpioPinDigitalOutput puenteH6L = gpio.provisionDigitalOutputPin(RaspiPin.GPIO_00, "LED11",PinState.LOW);
    GpioPinDigitalOutput puenteH6R = gpio.provisionDigitalOutputPin(RaspiPin.GPIO_07, "LED12",PinState.LOW);
    GpioPinDigitalOutput testigo = gpio.provisionDigitalOutputPin(RaspiPin.GPIO_15, "LED13",PinState.LOW);
    GpioPinDigitalOutput alarma_audible = gpio.provisionDigitalOutputPin(RaspiPin.GPIO_05, "BUZZER",PinState.LOW);

    //SWITCHS USUARIO
    GpioPinDigitalInput boton_seguro = gpio.provisionDigitalInputPin(RaspiPin.GPIO_24, "SEGURO", PinPullResistance.PULL_DOWN);
    GpioPinDigitalInput boton_accion = gpio.provisionDigitalInputPin(RaspiPin.GPIO_25, "OPEN/CLOSE", PinPullResistance.PULL_DOWN);

    //SWITCHS INDICADORES
    GpioPinDigitalInput i1A_2A = gpio.provisionDigitalInputPin(RaspiPin.GPIO_02, "SEGURO", PinPullResistance.PULL_DOWN);
    //GpioPinDigitalInput i2A = gpio.provisionDigitalInputPin(RaspiPin.GPIO_02, "SEGURO", PinPullResistance.PULL_DOWN);

    GpioPinDigitalInput i1D_2D = gpio.provisionDigitalInputPin(RaspiPin.GPIO_13, "SEGURO", PinPullResistance.PULL_DOWN);
    //GpioPinDigitalInput i1D = gpio.provisionDigitalInputPin(RaspiPin.GPIO_13, "SEGURO", PinPullResistance.PULL_DOWN);

    GpioPinDigitalInput i1E_2E = gpio.provisionDigitalInputPin(RaspiPin.GPIO_14, "SEGURO", PinPullResistance.PULL_DOWN);
    //GpioPinDigitalInput i2E = gpio.provisionDigitalInputPin(RaspiPin.GPIO_14, "SEGURO", PinPullResistance.PULL_DOWN);

    GpioPinDigitalInput i1B = gpio.provisionDigitalInputPin(RaspiPin.GPIO_03, "SEGURO", PinPullResistance.PULL_DOWN);
    GpioPinDigitalInput i1C = gpio.provisionDigitalInputPin(RaspiPin.GPIO_12, "SEGURO", PinPullResistance.PULL_DOWN);
    GpioPinDigitalInput i1F = gpio.provisionDigitalInputPin(RaspiPin.GPIO_21, "SEGURO", PinPullResistance.PULL_DOWN);
    GpioPinDigitalInput i1G = gpio.provisionDigitalInputPin(RaspiPin.GPIO_22, "SEGURO", PinPullResistance.PULL_DOWN);

    //GpioPinDigitalInput i2H = gpio.provisionDigitalInputPin(RaspiPin.GPIO_23, "SEGURO", PinPullResistance.PULL_DOWN);
    GpioPinDigitalInput i1H_2H = gpio.provisionDigitalInputPin(RaspiPin.GPIO_23, "SEGURO", PinPullResistance.PULL_DOWN);


    public void prueba(){
        while(eterno){
            if(finalizar()){
                if(boton_accion.getState().isHigh()){
                    System.out.print("Hola");
                    puenteH1L.pulse(5000);
                }
            }else{
                System.out.print("DETENER PROGRAMA");
            }
        }
    }


    public void detenerMotores(){
        puenteH1L.setShutdownOptions(true, PinState.LOW, PinPullResistance.OFF);
        puenteH1R.setShutdownOptions(true, PinState.LOW, PinPullResistance.OFF);
        puenteH2L.setShutdownOptions(true, PinState.LOW, PinPullResistance.OFF);
        puenteH2R.setShutdownOptions(true, PinState.LOW, PinPullResistance.OFF);
        puenteH3L.setShutdownOptions(true, PinState.LOW, PinPullResistance.OFF);
        puenteH3R.setShutdownOptions(true, PinState.LOW, PinPullResistance.OFF);
        puenteH4L.setShutdownOptions(true, PinState.LOW, PinPullResistance.OFF);
        puenteH4R.setShutdownOptions(true, PinState.LOW, PinPullResistance.OFF);
        puenteH5L.setShutdownOptions(true, PinState.LOW, PinPullResistance.OFF);
        puenteH5R.setShutdownOptions(true, PinState.LOW, PinPullResistance.OFF);
        puenteH6L.setShutdownOptions(true, PinState.LOW, PinPullResistance.OFF);
        puenteH6R.setShutdownOptions(true, PinState.LOW, PinPullResistance.OFF);
        testigo.setShutdownOptions(true, PinState.LOW, PinPullResistance.OFF);
        alarma_audible.setShutdownOptions(true, PinState.LOW, PinPullResistance.OFF);
        System.out.print("MOTORES DETENIDOS");
    }

    public boolean finalizar(){
        boolean status_seguro = boton_seguro.isHigh();
        boolean status_1h = i1D_2D.isHigh();
        boolean status_1d = i1D_2D.isHigh();
        if(status_seguro && status_1h && status_1d){
            detenerMotores();
            eterno = false;
            return false;
        }else{
            return true;
        }
    }




}
