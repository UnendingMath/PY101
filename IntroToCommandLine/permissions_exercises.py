# Exercise 1: Which user and group are assigned to the /etc folder on your computer?
# Command: ls -lah /etc; look for the . (current directory)
# root is the user and group

# Exercise 2: Which user and group are assigned to the $HOME folder?
# Command: ls -lah $HOME; look for the . (current directory)

# Exercise 3: What are mary's permissions for the napkins file in the following outputs?
# $ groups mary
# mary travelers vip
# $ ls -l custodian_closet
# total 0
# -rw-rw----  1 acmeair acmeair 0 Jul 21 17:57 napkins
# -rw-rw----  1 acmeair acmeair 0 Jul 21 17:57 paper_towels
# Mary falls in the "other" account permissions, meaning she has no access to napkin (---

# Exercise 4: What are mary's permissions to the donuts file in the following example:
# $ groups
# mary travelers vip
# $ ls -l vip_lounge
# $ ls -l ./
# ...
# -rw-rw----  1 acmeair  vip  0 Jul 21 17:57 donuts
# ...
# Mary has access to reading and writing, as she is a member of the vip group.

# Exercise 5: What are mary's permissions to the laptop file in the following example? What are the permissions for the group acmeinc?
# $ ls -l vip_lounge
# ...
# -r-xrwx---  1 mary acmeinc 0 Jul 21 17:57 laptop
# ...
# Mary is the user, meaning she has permissions to read and execute the laptop file
# The acmeinc group has permissions to read, write, and execute the laptop file.

# Exercise 6: Practice using sudo



