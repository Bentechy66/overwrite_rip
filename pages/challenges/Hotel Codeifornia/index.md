# Hotel Codeifornia
We found this machine running on the target's infrastructure. It could be an easy way to run some code, if we could just bypass the code-signing they've put in place.

We've also found a few combinations of code and signatures which are valid:
```
--------------------------------------
code: print("cool wind" in "my hair")
sign: 8bfd098cdcd21a26b6eaa63aa318bfc16d942d3889bad4755f3e3a8bd21fe6596b8c173504122615a6ea97639b8ade496abb1f9a66b7c131c1f8cd91fd126906711d19b8ce08fb8f2afae4de389f68e221db72bc06bac1e4c253e039fc9b8afffee74ca0748ca06e1ada65638745fb9681735212721072fd87d1877c6c32809c6512b89fab8d34408065af84e9bf783842b8ebbc4ca5269c62d79340d862dff7ea4da2a3b757d7c465c673bd8aa6cb68e54e5ac9847abf54c7da38aea49f8e0c131a97eb87f68ed760087d4a2fe9302cbf69881e57f1f0fd3e8925a635bf9239a8e50f9b1a416c4dbadd85fa54f2fab1737e614cf38b3299dff4564111308674
--------------------------------------
code: print("You can check out any time you like...")
sign: 6505f4751dd1d41f1820f421071ff63b9389386f15df6c592726166f062a24d617086fab9d57d04f191fef12a6173192f48f6fdf82a5463cd1d2582b4a43ba1c5b39291d2a7e0061e8ab66de0a6675dd517fa24a45f25e2f4a2cb7c67f471e885ef6491ece5f337d80f2d03b78f283946af229f4d937c0f0e6e8ec7946a9957e97760a6cfce461162b8f2d9376ff3382a2209a847a7468f68eb362c909368ca9dccd450884fe02ef7c8b4ce1314370a1ff7b5353735efe51849c40cbafbf7eb64435b0eb3b7d385ab083d624974d86baf0e0adce6a6f2693c9ef710e3d1bac3fbb7fadda48edbf2c9316fc4cbdc3d8efdf85a32b2b6a5dfc48bb89af24649f16
--------------------------------------
```

## Files
We managed to recover both the binary that's running on the server and the public key used to verify the signatures:
 - [pubkey.pem](pubkey.pem)
 - [hotel_codeifornia.elf](hotel_codeifornia.elf)

## Verify your solution
You should find a way to execute arbitrary code, only through interacting with stdin/stdout of hotel_codeifornia. You should place the pubkey in the same directory as the exe. You may not patch the binary or replace the public key.