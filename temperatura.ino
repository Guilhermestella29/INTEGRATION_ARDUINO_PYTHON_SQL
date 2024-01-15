#include <Thermistor.h>


int pinNTC = A1;

Thermistor temp(4); //VARIÁVEL DO TIPO THERMISTOR, INDICANDO O PINO ANALÓGICO (A2) EM QUE O TERMISTOR ESTÁ CONECTADO


void setup() {
  Serial.begin(9600); //INICIALIZA A SERIAL
  delay(1500); //INTERVALO DE 1 SEGUNDO
}
void loop() {
  
  int temperature = temp.getTemp(); //VARIÁVEL DO TIPO INTEIRO QUE RECEBE O VALOR DE TEMPERATURA CALCULADO PELA BIBLIOTECA
  Serial.print("Temperatura: ");//Imprime na serial o texto "Temperatura"
  Serial.print(temperature);//Imprime na serial o valor da temperatura calculada
  delay(1000);//Intervalo de 1 segundo
}
