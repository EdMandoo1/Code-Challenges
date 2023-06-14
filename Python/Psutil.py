#!/usr/bin/env python3
# Script Name:                  Psutil
# Author:                       Eduardo Ayala
# Date of latest revision:      06/14/23
# Purpose:                      Pulling system info using Psutil

import psutil

# Time spent by normal processes executing in user mode
user_time = psutil.cpu_times().user

# Time spent by processes executing in kernel mode
system_time = psutil.cpu_times().system

# Time when system was idle
idle_time = psutil.cpu_times().idle

# Time spent by priority processes executing in user mode
priority_user_time = psutil.cpu_times().nice

# Time spent waiting for I/O to complete
io_wait_time = psutil.cpu_times().iowait

# Time spent for servicing hardware interrupts
irq_time = psutil.cpu_times().irq

# Time spent for servicing software interrupts
softirq_time = psutil.cpu_times().softirq

# Time spent by other operating systems running in a virtualized environment
steal_time = psutil.cpu_times().steal

# Time spent running a virtual CPU for guest operating systems under the control of the Linux kernel
guest_time = psutil.cpu_times().guest

# Display the fetched information
print("Time spent by normal processes executing in user mode:", user_time)
print("Time spent by processes executing in kernel mode:", system_time)
print("Time when system was idle:", idle_time)
print("Time spent by priority processes executing in user mode:", priority_user_time)
print("Time spent waiting for I/O to complete:", io_wait_time)
print("Time spent for servicing hardware interrupts:", irq_time)
print("Time spent for servicing software interrupts:", softirq_time)
print("Time spent by other operating systems running in a virtualized environment:", steal_time)
print("Time spent running a virtual CPU for guest operating systems under the control of the Linux kernel:", guest_time)
