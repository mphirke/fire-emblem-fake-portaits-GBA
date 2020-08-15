# Generation of fake Fire Emblem GBA portraits using StyleGAN2
Seeing GANs create fake faces from real ones made me wonder could I create fake GBA fire emblem faces from the real ones. This repository is the result of that and it is purely non-commercial in nature.

<hr></hr>

## How do I use this?

1. [Click on this link](https://colab.research.google.com/drive/1gZLPmnc6c4r2LL46t6ZQ53BMrEnM_wyM?usp=sharing) and follow the instructions.
Alternatively, you could do it the long way and click on the file `
Demo_FE_GBA_Portraits.ipynb ` here on Github (scroll up) and then press the button `Open in Colab` when it shows up.

<hr></hr>

**Real examples of Fire Emblem GBA portaits:**
![Real Fire Emblem Portraits GBA](https://raw.githubusercontent.com/mphirke/fire-emblem-fake-portaits-GBA/master/media/Reals_example.png)


**Thanks to spriters for providing the training data:**
1. [Aegius (Zach)](https://feuniverse.us/u/Aegius) who gave ~30 portraits from his [project (Necrosis Among the Living).](https://feuniverse.us/t/necrosis-among-the-living/8815)
2. [Fire Emblem Mugs](https://www.deviantart.com/atey/art/Fire-Emblem-Mugs-216376087) by [Atey](https://www.deviantart.com/atey) who has posted the linked portraits for use freely.
3. [Servants from FateGO in the GBA portrait style](https://www.reddit.com/r/fireemblem/comments/c1c74a/servants_from_fatego_in_the_gba_portrait_style/), [Collection of Fire Emblem Fates GBA Mugs](https://www.reddit.com/r/fireemblem/comments/4b0ra9/collection_of_fire_emblem_fates_gba_mugs/), [Nohr in GBA Style](https://www.reddit.com/r/fireemblem/comments/3xmweg/nohr_in_gba_style/) by u/[Toaomr](https://www.reddit.com/user/Toaomr) on Reddit and Twitter : [@toaomr](https://twitter.com/toaomr)
4. [Fire Emblem Custom mug GBA spread sheet](https://www.deviantart.com/caringcarrot/art/Fire-Emblem-Custom-mug-GBA-Sprite-Sheet-804177772) by [caringcarrot](https://www.deviantart.caom/caringcarrot)
5. Free to use NICKT collection by [NICKT](https://feuniverse.us/u/NICKT)

If you intend to use those sprites for training, please ask the artists. I will not redistribute their works so don't ask me. If you want to add your own sprites and train, remember, the input to StyleGAN must be a square image(with dimensions in power of 2, so example valid size is 64x64, 128x128, 32x32, etc), and all inputs must have the same size, so if you are using half-bodies, for example, you will have to crop and resize them down.

**Generated Fakes Example (480 kimg):** <br></br> 

![Some handpicked fakes](https://raw.githubusercontent.com/mphirke/fire-emblem-fake-portaits-GBA/master/media/fakes_example.png)


![Generated Fakes Example](https://raw.githubusercontent.com/mphirke/fire-emblem-fake-portaits-GBA/master/media/fakes0469_example.png)

<hr></hr>

**Generated Fakes training (from 0th kimg to 480th kimg) video on YouTube:**  

<div align="center">
  <a href="https://www.youtube.com/watch?v=DKpNqQ-9sAI"><img src="https://www.dropbox.com/s/j4fvh1rxqtjcr3y/FE_video_thumbnail.png?raw=1" alt="IMAGE ALT TEXT"></a>
</div>

<hr></hr>

This is still a work in progress.
To Do:

 - [x] Preprocess images automatically to 128x128 and turn background white
 - [ ] Get more images to train on
 - [x] Create another notebook to generate output for demo purposes.

<hr></hr>

**License**

This project was purely made for educational purposes/research purposes and the code base is strictly non-commercial as it is licensed under [Nvidia Source Code License-NC](https://github.com/mphirke/fire-emblem-fake-portaits-GBA/blob/master/LICENSE.md) because of usage of StyleGAN2. You are free to use (credit appreciated but not required) this tool as long as you use it reponsibly and non-commerically but we are not responsible for any uses (read the license for more details). Do not ask us for the training dataset. We do not have the permission to redistribute the artists'  works.

**References:**

 1. [Steam StyleGAN2 by woctezuma](https://github.com/woctezuma/steam-stylegan2)
 2. [The original StyleGAN2 repository](https://github.com/NVlabs/stylegan2)
 3. [@woctezuma](https://github.com/woctezuma)'s [fork of StyleGAN2 for easy saving results in google drive.](https://github.com/woctezuma/stylegan2)

StyleGAN2 citation:

```
@article{Karras2019stylegan2,
  title   = {Analyzing and Improving the Image Quality of {StyleGAN}},
  author  = {Tero Karras and Samuli Laine and Miika Aittala and Janne Hellsten and Jaakko Lehtinen and Timo Aila},
  journal = {CoRR},
  volume  = {abs/1912.04958},
  year    = {2019},
}
```


