---
layout: default
title: PCB design best practices 
has_children: true
---

# PCB design best practices


## USB C
Soldering a 16-pin USB C 16-Pin SMT receptacle is very difficult.
6-pin SMT or 16-pin through hole is a better choice:

| 6-pin SMT | 16-pin THT | 
| :-------------: |:-------------:| 
| [![](images/10pcs-lot-Type-C-6-Pin-USB-SMT-Socket-Connector-USB-3-1-Type-C-Female.jpg_Q90.jpg)](https://www.aliexpress.com/item/4000896345613.html?spm=a2g0o.productlist.0.0.73054a2aPJUuTl&algo_pvid=d5f3049e-9c74-497e-a3ea-b00348b9c7cd&algo_expid=d5f3049e-9c74-497e-a3ea-b00348b9c7cd-4&btsid=0b0a050116187473309053224e7a47&ws_ab_test=searchweb0_0,searchweb201602_,searchweb201603_) | [![](images/10-pcs-USB-Type-C-3-1-Receptacle-16-Pin-DIP-Horizontal-Edge-PCB-Connector-Female.jpg_Q90.jpg)](https://www.aliexpress.com/item/4000967090640.html?spm=a2g0o.productlist.0.0.73054a2aPJUuTl&algo_pvid=d5f3049e-9c74-497e-a3ea-b00348b9c7cd&algo_expid=d5f3049e-9c74-497e-a3ea-b00348b9c7cd-9&btsid=0b0a050116187473309053224e7a47&ws_ab_test=searchweb0_0,searchweb201602_,searchweb201603_) | 

## Underside Pads
Consider the popular nRF52840 E73-2G4M08S1C module.
It has a small footprint aided by the pads underneath.
This can be hand solderable by having holes through the PCB.
The holes should be as large as possible, the ones in the footprint here were too small.

| Top | Bottom | Footprint |
| :---: | :---: | :---:|
| ![](images/e73_top.jpg) | ![](images/e73_bottom.jpg) | ![](images/e73_footprint.jpg) |

I would recommend using modules with just castellated edges.

## Useful Resources
- https://github.com/rafaeldelboni/buildlogs/blob/main/torn-v3.md
- https://github.com/hsgw/plaid