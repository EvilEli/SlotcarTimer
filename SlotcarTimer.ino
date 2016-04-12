// Timer with interrupt
//
// Copyright: Elias Rosch <eliasrosch@googlemail.com>

#define INTERRUPT_INTERVALL 3000
#define LED_GREEN 4
#define LED_RED 5
#define LED_BLUE 6

enum e_timer_state_t {
  E_TIMER_STATE_START,
  E_TIMER_STATE_START_SEQ,
  E_TIMER_STATE_JUMP_START,
  E_TIMER_STATE_TIMING,
  E_TIMER_STATE_FINISH,
};

volatile unsigned long last_int0=0, last_int1=0;
unsigned long time_0=0, last_time_0, time_1=0, last_time_1, start_time, pb_0 = 999999999, pb_1 = 999999999, overall_best = 999999999;
e_timer_state_t state = E_TIMER_STATE_START;
bool new_time_0=false, new_time_1=false;
uint8_t lap_0 = 0, lap_1 = 0;
char serial_command;

bool light_is_on;

void init_start_seq(){
  start_time = millis();
  digitalWrite(LED_RED, HIGH);
  while (millis()-start_time < 200){
    if (state == (E_TIMER_STATE_JUMP_START)) return;
  }
  digitalWrite(LED_RED, LOW);
  while (millis()-start_time < 1200){
    if (state == (E_TIMER_STATE_JUMP_START)) return;
  }
  digitalWrite(LED_RED, HIGH);
  while (millis()-start_time < 1400){
    if (state == (E_TIMER_STATE_JUMP_START)) return;
  }
  digitalWrite(LED_RED, LOW);
  while (millis()-start_time < 2400) {
    if (state == (E_TIMER_STATE_JUMP_START)) return;
  }
  digitalWrite(LED_RED, HIGH);
  while (millis()-start_time < 2600) {
    if (state == (E_TIMER_STATE_JUMP_START)) return;
  }
  digitalWrite(LED_RED, LOW);
  while (millis()-start_time < 3600) {
    if (state == (E_TIMER_STATE_JUMP_START)) return;
  }

  unsigned long current_time = millis();
  lap_0 = 0;
  lap_1 = 0;
  time_0 = current_time;
  time_1 = current_time;
  last_time_0 = current_time;
  last_time_1 = current_time;
  start_time = millis();
  state = E_TIMER_STATE_TIMING;
  light_is_on = true;
  digitalWrite(LED_GREEN, HIGH);
}

void setup() {
  pinMode(2, INPUT);       // Pin 2
  pinMode(3, INPUT);       // Pin 3
  digitalWrite(2, HIGH);   // internal pull-up to 5V
  digitalWrite(3, HIGH);   // internal pull-up to 5V
  attachInterrupt(0, interruptRoutine0, HIGH);
  attachInterrupt(1, interruptRoutine1, HIGH);

  pinMode(4, OUTPUT);       // Pin 4
  pinMode(5, OUTPUT);       // Pin 5
  pinMode(6, OUTPUT);       // Pin 6
  digitalWrite(4, LOW);
  digitalWrite(5, LOW);
  digitalWrite(6, LOW);
  Serial.begin(115200);
  Serial.println("READY!");
}

void loop() {
  switch(state) {
    case E_TIMER_STATE_START:
      if (Serial.available()){
        if (Serial.read() == 'S'){
          state = E_TIMER_STATE_START_SEQ;
          Serial.println("Now starting!");
          //Serial.println("Now in timing mode!");
        }
      }
      break;
    case E_TIMER_STATE_START_SEQ:
      init_start_seq();
      break;
    case E_TIMER_STATE_TIMING:
      serial_command = Serial.read();
      if (serial_command == 'S'){
          state = E_TIMER_STATE_START_SEQ;
          Serial.println("Now starting!");
          break;
          //Serial.println("Now in timing mode!");
      }
      if (light_is_on && (millis() - start_time > 1000)){
        digitalWrite(LED_GREEN, LOW);
        digitalWrite(LED_RED, LOW);
        digitalWrite(LED_BLUE, LOW);
        light_is_on = false;
      }
      
      if (new_time_0){
        if ((time_0 - last_time_0 < overall_best) && (lap_0 > 1)) {
          overall_best = time_0 - last_time_0;
          pb_0 = time_0 - last_time_0;
          start_time = millis();
          digitalWrite(LED_RED, HIGH);
          digitalWrite(LED_BLUE, HIGH);
          light_is_on = true;
        } else if ((time_0 - last_time_0 < pb_0) && (lap_0 > 1)) {
          pb_0 = time_0 - last_time_0;
          start_time = millis();
          digitalWrite(LED_GREEN, HIGH);
          light_is_on = true;          
        }
        Serial.print("S0;");
        Serial.print((time_0-last_time_0)/1000);
        Serial.print(";");
        Serial.print((time_0-last_time_0)%1000);
        Serial.print(";");
        Serial.println(lap_0-1);
        new_time_0 = false;
      }
      
      if (new_time_1){
        if ((time_1-last_time_1 < overall_best) && (lap_1 > 1)) {
          overall_best = time_1 - last_time_1;
          pb_1 = time_1 - last_time_1;
          start_time = millis();
          digitalWrite(LED_RED, HIGH);
          digitalWrite(LED_BLUE, HIGH);
          light_is_on = true;
        } else if ((time_1 - last_time_1 < pb_1) && (lap_1 > 1)) {
          pb_1 = time_1 - last_time_1;
          start_time = millis();
          digitalWrite(LED_GREEN, HIGH);
          light_is_on = true;          
        }
        Serial.print("S1;");
        Serial.print((time_1-last_time_1)/1000);
        Serial.print(";");
        Serial.print((time_1-last_time_1)%1000);
        Serial.print(";");
        Serial.println(lap_1-1);
        new_time_1 = false;
      }
      break;
    case E_TIMER_STATE_FINISH:
      while(true);
    case E_TIMER_STATE_JUMP_START:
      while(true);
      break;
  }
}

void interruptRoutine1() {
  unsigned long current_time = millis();
  if(state == E_TIMER_STATE_START_SEQ){
    state = E_TIMER_STATE_JUMP_START;
    Serial.println("J0");
    digitalWrite(LED_RED, HIGH);
    digitalWrite(LED_GREEN, HIGH);
  }
  else if((current_time - last_int0) > INTERRUPT_INTERVALL) { 
    lap_0 += 1;
    new_time_0 = true;
    last_int0 = current_time;
    last_time_0 = time_0;
    time_0 = current_time;      
  }
}

void interruptRoutine0() {
  unsigned long current_time = millis();
  if(state == E_TIMER_STATE_START_SEQ){
    state = E_TIMER_STATE_JUMP_START;
    Serial.println("J1");
    digitalWrite(LED_RED, HIGH);
    digitalWrite(LED_GREEN, HIGH);
  }
  else if((current_time - last_int1) > INTERRUPT_INTERVALL) {
    lap_1 += 1;
    new_time_1 = true;
    last_int1 = current_time;
    last_time_1 = time_1;
    time_1 = current_time; // letzte Schaltzeit merken
  }
}
