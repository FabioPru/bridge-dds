/*
   DDS, a bridge double dummy solver.

   Copyright (C) 2006-2014 by Bo Haglund /
   2014-2016 by Bo Haglund & Soren Hein.

   See LICENSE and README.
*/


// Test program for the CalcAllTablesPBN function.
// Uses the hands pre-set in hands.cpp.

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "../include/dll.h"
#include "hands.h"

#include <iostream>
#include <iomanip>
#include <algorithm>

#include "../test/print.h"
#include "../test/cst.h"


int no_hands = 1;

char enc (int x) {
  if (x < 10) { return '0' + x; }
  return 'A' + (x - 10);
}

char MYPBN[1][80] = {
  "N:T9854..QT52.AT94 Q2.KQ98.AJ87.532 KJ6.J76532.4.J87 A73.AT4.K963.KQ6"
};

void print_TABLE(const ddTableResults& table)
{
  // ORDINE :::: NT, S, H, D, C   played by SENW

  std::cout << enc(13 - table.resTable[4][2]) << enc(table.resTable[4][1]) << enc(13 - table.resTable[4][0]) << enc(table.resTable[4][3]);

  for (int suit = 0; suit <= 3; suit++)
  {
    std::cout << enc(13 - table.resTable[suit][2]) << enc(table.resTable[suit][1]) << enc(13 - table.resTable[suit][0]) << enc(table.resTable[suit][3]);
  }
}


int main()
{
  ddTableDealsPBN DDdealsPBN;
  ddTablesRes tableRes;
  allParResults pres;

  int mode = 0; // No par calculation
  int trumpFilter[DDS_STRAINS] = {0, 0, 0, 0, 0}; // All
  int res;
  char line[80];
  bool match;

  #if defined(__linux) || defined(__APPLE__)
    SetMaxThreads(0);
  #endif

  DDdealsPBN.noOfTables = 1;

  int N; char c;
  std::cin >> N;

  for (int j = 0; j < N; j++) {
  
    for (int t = 2; t < 69; t++) {
        if ((t == 18) || (t == 35) || (t == 52) || (t == 69)) { continue; }
        std::cin >> c;
        MYPBN[0][t] = c;
    }

  strcpy(DDdealsPBN.deals[0].cards, MYPBN[0]);

  res = CalcAllTablesPBN(&DDdealsPBN, mode, trumpFilter,
                         &tableRes, &pres);

  if (res != RETURN_NO_FAULT)
  {
    ErrorMessage(res, line);
    printf("DDS error: %s\n", line);
  }

  std::cout << DDdealsPBN.deals[0].cards << ":"; 
  print_TABLE(tableRes.results[0]);
  std::cout << "\n";

  }
}

