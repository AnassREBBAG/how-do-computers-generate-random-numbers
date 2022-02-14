# how-do-computers-generate-random-numbers

You may be wondering how acomputer can actually generate a random number . With no input given , where does this “randomness” come from?
To generate a “true” random number, the computer measures some type of physical phenomenon that takes place outside of the computer. For example, the computer could measure the
radioactive decay of an atom. According to quantum theory, there’s no way to know for sure when radioactive decay will occur, so this is essentially “pure randomness” from the
universe. An attacker wouldn’t be able to predict when radioactive decay would occur, so they wouldn’t know the random value.
The computer could rely on atmospheric noise or simply use the exact time you press keys on your keyboard as a source of unpredictable data, or entropy. For example, your computer
might notice that you pressed a key at exactly 0.23423523 seconds after 2 p.m,by observing some outside data, like mouse movements or fan noise, which is not predictable, and
creating data from it. This is known as entropy.
Other times, they generate “pseudorandom” numbers by using an algorithm so the results appear random,
