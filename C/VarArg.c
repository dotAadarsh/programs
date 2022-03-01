//https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/va-arg-va-copy-va-end-va-start?view=msvc-170

#include<stdarg.h>
#include<stdio.h>

double avg(int num, ...) {
  va_list arguments;
  double sum =0;

  va_start (arguments,num);
    for(int i=0;i<num;i++)
      sum+=va_arg(arguments,double);
  va_end(arguments);

  return sum/num;
}

int main(){
  printf("%f\n",avg(1,2,3.4,4.4,5));
}