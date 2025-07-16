**Hash_Collision_Finder**

If you are a Competitive Programmer or into it, then you must be aware of String Hashing, since many users uses only 1 Hashing which can be easily hacked by Using the concept of __BirthdayAttack__ Highly used in Cyrptography ,  particularly in the context of __hash functions__ .
Our Logic is Simple for it

1) Write a function to calculate the hash value
2) Write a random generator of string
3) When there are k possible distinct hash values, look up O(k−−√) random candidates
4) Now we get a pair of strings that has exactly the same hash value!

In this method, the only things we should consider are that k is small enough (around k≤1012 ), and the number of possible candidates is large enough. We don't need to care about what the hashing function is!

__How to Use it__(On Linux(Ubuntu Distro) Terminal)

1) Open Terminal and Type `nano hash_collision_finder.cpp`
2) After Writing this Code Press `Ctrl+X Ctrl+Y` to save it.
3) Write this `g++ -O2 -std=c++17 hash_collision_finder.cpp -o hash_collision_finder` to compile it
4) Write this `./hash_collision_finder`

   <img width="810" height="569" alt="image" src="https://github.com/user-attachments/assets/04adb51c-8a01-434c-b503-c3cd28420f82" />
