#include <stdio.h>
#include <math.h>

#define MAX 20

typedef struct __elev
{
  int name;
  int passenger;
  int direction;
  int destination;
  int location;
} elev;

int elevAssign(elev* elevArr, int start, int end, int people)
{
  int elevNumber;
  int i = 0; int j = 0;
  int leastTmp = 0;
  elev changeTmp;
  elevNumber = sizeof(elevArr);

  //sort
  for(i = 0; i < elevNumber; i++)
  {
    for(j = i; j < elevNumber; j++)
    {
      if(abs((elevArr+i)->location-start) > abs((elevArr+j)->location-start))
      {
        leastTmp = j;
      }
      else
      {
        leastTmp = i;
      }
      changeTmp = elevArr[i];
      elevArr[i] = elevArr[j];
      elevArr[j] = changeTmp;
    }
  }

  for(i = 0; i < elevNumber; i++)
  {
    if ((people + (elevArr+i)->passenger) > MAX)
    {
      continue;
    }
    if ((end-start) * (((elevArr+i)->location - start) * (elevArr+i)->direction < 0))
    {
      continue;
    }
    return (elevArr+i)->name;
  }

  //sort
  i = 0;
  for(j = 0; j < elevNumber; j++)
  {
    if(abs((elevArr+i)->destination-start) > abs((elevArr+j)->destination-start))
    {
      leastTmp = j;
    }
    else
    {
      leastTmp = i;
      }
    changeTmp = elevArr[i];
    elevArr[i] = elevArr[j];
    elevArr[j] = changeTmp;
  }
  return elevArr->name;

}

int main(void)
{

}
