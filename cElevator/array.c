#include <stdio.h>
#include <stdlib.h>
#include "array.h"



void arrayAdd(int array[], int data){
  if (array = NULL)
  {
    array = (int*)malloc(sizeof(int));
    array[0] = data;
  } else
  {
    array = (int*)realloc(array, sizeof(array) + sizeof(int));
    array[sizeof(array)/sizeof(int)-1] = data;
  }
}

void arraySort(int array[]){
  int num = sizeof(array)/sizeof(int);
  int i = 0; int j = 0; int tmp;

  for(i = 0; i < num; i++)
  {
    for(j = i; j < num; j++)
    {
      if(array[i]>array[j])
      {
        tmp = array[j];
        array[j] = array[i];
        array[i] = tmp;
      }
    }
  }
}

void arrayDelete(int array[], int data){

  for (i = 0; i < num; i++)
  {
    if(array[i] == data)
    {
      break;
    }
  }

  for(i = i; i < num-1; i++)
  {
    array[i] = array[i+1];
  }
  array[i] = 0;
}
