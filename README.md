# Generation of fake Fire Emblem GBA portraits using StyleGAN2
Seeing GANs create fake faces from real ones made me wonder could I create fake GBA fire emblem faces from the real ones. This repository is the result of that and it is purely non-commercial in nature.

**Real examples of Fire Emblem GBA portaits:**
![Real Fire Emblem Portraits GBA](https://raw.githubusercontent.com/mphirke/fire-emblem-fake-portaits-GBA/master/media/Reals_example.png)

The reals (training) dataset consists of:
1. [Vanilla Fire Emblem GBA Sprites](https://cdn.discordapp.com/attachments/206588291053649921/423956771845963786/p.png)
2. [Fire Emblem Mugs](https://www.deviantart.com/atey/art/Fire-Emblem-Mugs-216376087) by [Atey](https://www.deviantart.com/atey) who has posted the linked sprites for use freely.
3. [Servants from FateGO in the GBA portrait style](https://www.reddit.com/r/fireemblem/comments/c1c74a/servants_from_fatego_in_the_gba_portrait_style/), [Collection of Fire Emblem Fates GBA Mugs](https://www.reddit.com/r/fireemblem/comments/4b0ra9/collection_of_fire_emblem_fates_gba_mugs/), [Nohr in GBA Style](https://www.reddit.com/r/fireemblem/comments/3xmweg/nohr_in_gba_style/) by u/[Toaomr](https://www.reddit.com/user/Toaomr) on Reddit and Twitter : [@toaomr](https://twitter.com/toaomr)

I am in process of updating the dataset with more images soon to achieve more variety in results.


If you intend to use those sprites for training, please ask the artists for permission before you use their sprites. Remember, the input to StyleGAN must be a square (with power of 2, so example valid size is 64x64, 128x128, 32x32, etc), and all inputs must have the same size, so if you are using half-bodies, for example, you will have to crop and resize them down.

**Generated Fakes Example (469th kimg):**
![Generated Fakes Example](https://raw.githubusercontent.com/mphirke/fire-emblem-fake-portaits-GBA/master/media/fakes0469_example.png)

### I will update the examples as the training continues, but for now I cannot use Colab GPU for a while. (Current progress: 9 hours training on Colab, 469 kimgs passed). 


**Generated Fakes training (from 112th kimg to 469th kimg) video on YouTube:**

<div align="center">
  <a href="https://www.youtube.com/watch?v=mLYMi5cOCaw"><img src="https://www.dropbox.com/s/j4fvh1rxqtjcr3y/FE_video_thumbnail.png?raw=1" alt="IMAGE ALT TEXT"></a>
</div>

This is still a work in progress.
To Do:

 - [x] Preprocess images automatically to 128x128 and turn background white
 - [ ] Get more images to train on
 - [ ] Create another notebook to generate output for demo purposes.

**References:**

 1. [Steam StyleGAN2 by woctezuma](https://github.com/woctezuma/steam-stylegan2)
 2. [The original StyleGAN2 repository](https://github.com/NVlabs/stylegan2)
 3. [@woctezuma](https://github.com/woctezuma)'s [fork of StyleGAN2 for easy saving results in google drive.](https://github.com/woctezuma/stylegan2)

