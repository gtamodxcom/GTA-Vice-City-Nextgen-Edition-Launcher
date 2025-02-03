<template>
  <v-container>
    <v-card class="mx-auto">
      <v-img src="/assets/Nextgen.png" cover></v-img>
      <v-card-title>
        GTAMODX
      </v-card-title>

      <v-card-subtitle>
        罪恶都市次世代版 中文启动器
      </v-card-subtitle>

      <v-card-actions>
        <v-btn :icon="show ? 'mdi-chevron-up' : 'mdi-chevron-down'" @click="show = !show"></v-btn>

        <v-spacer></v-spacer>
        <v-btn color="blue" onclick="selectDirectory()">
          选择目录
          <v-tooltip activator="parent" id="directory "
            location="top">选择游戏的安装目录</v-tooltip>
        </v-btn>
        <v-btn color="orange-lighten-2" onclick="openGames()">
          启动游戏
          <v-tooltip activator="parent"
            location="top">Ciallo～(∠・ω< )⌒☆</v-tooltip>
          </v-btn>

      </v-card-actions>

      <v-expand-transition>
        <div v-show="show">
          <v-divider></v-divider>

          <v-card-text v-html="Info">
          </v-card-text>
        </div>
      </v-expand-transition>
    </v-card>

    <v-row id="Tomori">
      <v-col cols="12" sm="6" style="margin-top: 10px;">
        <v-card class="mx-auto pa-2" image="/assets/Bridge_view.webp" subtitle="前往哔哩哔哩查看游戏实机演示视频" title="实机演示">
          <template v-slot:actions>
            <v-btn append-icon="mdi-chevron-right" color="red-lighten-2" text="立即观看" variant="outlined" block
              @click="GameVideo"></v-btn>
          </template>
        </v-card>
      </v-col>
      <v-col cols="12" sm="6" style="margin-top: 10px;">
        <v-card class="mx-auto pa-2" image="/assets/Ocean_Drive.webp" subtitle="如果您还没有游戏请前往GTAMODX不限速下载罢!" title="下载游戏">
          <template v-slot:actions>
            <v-btn append-icon="mdi-chevron-right" color="red-lighten-2" text="立即下载" variant="outlined" block
              @click="DownloadUrl"></v-btn>
          </template>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>
<style>
#Tomori .v-img__img--cover {
  opacity: 0.5;
}
</style>
<script lang="ts">
export default {
  data: () => ({
    show: false,
    Info: `
<h2>机翻说明：</h2>
<br>
<p>《GTA Vice City Nextgen Edition》是基于《GTA IV》的RAGE游戏引擎进行的全球修改。这个模组不仅仅是将这座城市转换为该系列的下一部分。这个模组是原始游戏中所有任务的完整转移。由于RAGE引擎的物理和机械性能的改进，这将提供一种全新的游戏体验。</p>
<p>官方重制版仅使用虚幻引擎进行渲染，但游戏的物理引擎仍然是20多年前发布的RenderWare，其机制和动画已经过时。</p>
<p>我们正在使用下一代发动机。是的，不是它的最新版本，而是唯一一个可以用原始情节进行修改的版本。这就是为什么这个模组被称为Nextgen Edition。</p>
<p>我们努力将游戏前几个版本中最好的元素结合在一起，让心爱的《罪恶之城》焕发出新的色彩。这让粉丝们有机会回到熟悉的世界和故事中，同时体验新鲜的情感和玩他们最喜欢的游戏的新视角。</p>
<p>在这个版本的mod中，有以下功能可用：</p>
<p>所有故事任务完全从头开始编写</p>
<p>RAGE引擎上功能齐全的游戏过场动画</p>
<p>城市服务的所有额外任务</p>
<p>在海曼纪念体育场的赛车任务</p>
<p>阳光汽车的赛车任务</p>
<p>阳光汽车进口车库的附加任务</p>
<p>在Top Fun面包车中执行遥控车辆任务</p>
<p>特技跳跃</p>
<p>隐藏的包裹</p>
<p>原始游戏中的完整chets</p>
<p>从最终版改进版的城市</p>
<p>《Vice City Stories》中的建筑霓虹灯</p>
<p>从最终版改进的武器</p>
<p>Xbox版本的所有车辆</p>
<p>来自GTA圣安德烈亚斯的几辆额外汽车（适合大气层）</p>
<p>Xbox版本中所有角色和道具的模型（具有改进的纹理）</p>
<p>PS2版本的所有原始广播电台（带有剪辑曲目《莱昂内尔·里奇-与夜同行》）</p>
<p>以原版《罪恶之城》的风格加载屏幕和游戏内设计（包括100%完成游戏）</p>
<p>我们团队提供了额外的修复、改进和几个复活节彩蛋</p>
<p><br></p>
<p>开发团队：</p>
<p>-LaV07</p>
<p>Derial Brown</p>
<p>-AndrewMulti</p>
<p>Hot Dam</p>
<p><br></p>
<p>免责声明：此修改完全免费，没有任何商业利益。该项目是由粉丝为粉丝创建的。革命团队对原版游戏的开发者表示感谢。游戏过程中可能会出现错误和崩溃，因为这是一个粉丝制作的模组，而不是官方的重制版。</p>
    `,
  }),
  methods: {
    DownloadUrl() {
      window.open('https://www.gtamodx.com/announcement-9', '_blank');
    },
    GameVideo() {
      window.open('https://www.bilibili.com/video/av113895217895012', '_blank');
    }
  }
}
</script>
