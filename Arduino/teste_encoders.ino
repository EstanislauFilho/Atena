//Programa: Motor DC com encoder
//Autor: Arduino e Cia

const byte Encoder_C1 = 2;
const byte Encoder_C2 = 4;
byte Encoder_C1Last;
int duracao;
boolean Direcao;

//Pinos de ligacao ponte H L298N
#define pino_motor1 6
#define pino_motor2 7

void setup()
{
  Serial.begin(57600);
  //Pino potenciometro
  pinMode(A0, INPUT);
  //Definicao pinos ponte H
  pinMode(pino_motor1, OUTPUT);
  pinMode(pino_motor2, OUTPUT);
  //Definicao do encoder
  EncoderInit();
}

void loop()
{
  Serial.print("Pulso: ");
  Serial.print(duracao);
  int valor = analogRead(A0);
  if (valor >= 512)
  {
    digitalWrite(pino_motor1, LOW);
    digitalWrite(pino_motor2, LOW);
    //delay(1000);
    digitalWrite(pino_motor1, LOW);
    digitalWrite(pino_motor2, HIGH);
    Serial.println(" Sentido: Anti-horario");
  }
  else
  {
    digitalWrite(pino_motor1, HIGH);
    digitalWrite(pino_motor2, LOW);
    Serial.println(" Sentido: Horario");
  }
  duracao = 0;
  delay(100);
}

void EncoderInit()
{
  pinMode(Encoder_C2, INPUT);
  attachInterrupt(0, calculapulso, CHANGE);
}

void calculapulso()
{
  int Lstate = digitalRead(Encoder_C1);
  if ((Encoder_C1Last == LOW) && Lstate == HIGH)
  {
    int val = digitalRead(Encoder_C2);
    if (val == LOW && Direcao)
    {
      Direcao = false; //Reverse
    }
    else if (val == HIGH && !Direcao)
    {
      Direcao = true;  //Forward
    }
  }
  Encoder_C1Last = Lstate;

  if (!Direcao)  duracao++;
  else  duracao--;
}
