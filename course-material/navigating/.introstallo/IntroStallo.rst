Stallo - introduction

Name: Named after the strongest monster from Sami mythology; the most powerful monster in the region. 

Supercomputer vs computer: Size!
* Slightly organized differently
* Usage

* Stallo: 776 nodes, 14304 compute cores, 27 TB ram, 2.1PB disk
* Desktop: 1-2 nodes, 4-8 compute cores, 6-8 GB ram, 500-1000 GB disk.

Implications from size:
”Organs” more pronounced.
More than one disk/file system.
Stripped/easy to maintain OS (=LINUX in this case)
Since the machine is large and expensive; you must expect to share.

* Job-distribution system, also called batch system (dividing all tasks into batches and distribute on the system).

More than one network
More than one file system

Different servers for:
Login and job distributions
Compute
File system handling
(Administration)

Huge difference on total memory and available memory to share on one compute node (a.k.a one machine).
Speed difference on different networks.
(Why you should allways run jobs on /global/work)

When you need hpc:

Large scale calculations; large in terms of
A lot of compute cores
A lot of wall-clock time
A lot of memory
A lot of temporary disk

(A lot of disk/storage)

And of course: The power set of the intersection of all the above sets.

More info:

http://hpc.uit.no/en/latest/
http://hpc.uit.no/en/latest/stallo/stallo.html
http://hpc.uit.no/en/latest/account/account.html
 
http://hpc.uit.no/en/latest/software/applications.html
http://hpc.uit.no/en/latest/applications/sw_guides.html

For many HPC related problems; Google is your friend…

