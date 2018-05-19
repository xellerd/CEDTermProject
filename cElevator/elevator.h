#ifndef __ELEVATOR_H__
#define __ELEVATOR_H__

#define MAX 10
#define LINE 3
#define FLOOR 14

typedef struct __elevator{
  int psg;
  int loc;
  int * dest;
}elevator;

typedef struct __passenger{
  int psg;
  int stt;
  int fin;
}passenger;

typedef struct __elog{
  int time;
  int start[];
  int stop[];
}elog;

void call(elevator* e, passenger* p);

void ride(elevator* e, passenger* p);

void move(elevator* e, elog* log);

void stop(elevator* e, elog* log);


#endif
