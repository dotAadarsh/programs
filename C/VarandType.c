#include<stdio.h>
 int main(int argc, char *argv[]){
   int distance = 100;
   float power = 2.345f;
   double super_power = 56785.3456;
   char initial = 'M';
   char first_name[] = "Mad";
   char last_name[] = "Max";

   printf("You are %d miles away\n", distance);
   printf("You have %f levels of power\n", power);
   printf("You have %lf awesome super power\n", super_power);
   printf("I have an initial %c\n", initial);
   printf("I have a first name %s\n", first_name);
   printf("I have a last name %s\n", last_name);

   unsigned long universe_of_defects = 1L * 1024L * 1024L * 1024L;
   printf("The entire universe has %ld\n", universe_of_defects);

   char null_byte = '\0';
   int care_percentage = 10 * null_byte;
   printf("Which means you should care %d%%.\n", care_percentage);
 }