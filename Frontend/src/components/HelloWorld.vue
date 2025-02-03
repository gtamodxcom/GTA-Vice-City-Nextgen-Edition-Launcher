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
          <v-tooltip activator="parent" id="directory " location="top">选择游戏的安装目录</v-tooltip>
        </v-btn>
        <v-btn color="orange-lighten-2" onclick="openGames()">
          启动游戏
          <v-tooltip activator="parent" location="top">Ciallo～(∠・ω< )⌒☆</v-tooltip>
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
<h2>说明：</h2>
<br>
<p>GTA Vice City Nextgen Edition 是一款基于《GTA IV》RAGE游戏引擎开发的全球性模组。该模组不仅是对城市场景的简单移植，而是完整复刻了原版游戏的所有任务。借助RAGE引擎升级的物理效果和游戏机制，玩家将获得焕然一新的游戏体验。
    <br />
    <br />
    官方重制版仅使用虚幻引擎进行画面渲染，但其物理引擎仍沿用20多年前发布的RenderWare系统，包含过时的游戏机制和动画效果。
    <br />
    <br />
    我们采用次世代引擎开发。虽然并非最新版本，但这是唯一能实现原版剧情模组改造的可行方案。因此本模组被命名为Nextgen Edition（次世代版）。
    <br />
    <br />
    我们致力于整合历代版本的最佳元素，让玩家熟悉的罪恶都市以全新姿态焕发光彩。这为粉丝们提供了重返经典世界的机会，在重温原汁原味故事的同时，体验充满新鲜感的全新游戏视角。
    <br />
    <br />
    当前版本包含以下特色内容：
    <br />
    • 完全重构的主线任务
    <br />
    • RAGE引擎打造的全动态过场动画
    <br />
    • 完整的城市服务支线任务
    <br />
    • 海曼纪念体育场竞速赛事
    <br />
    • 阳光车行汽车挑战赛
    <br />
    • 阳光车行进口车库特别任务
    <br />
    • 顶趣（Top Fun）厢型车遥控载具任务
    <br />
    • 特技跳跃挑战
    <br />
    • 隐藏包裹收集
    <br />
    • 原版完整作弊系统
    <br />
    • 基于最终版优化的城市建模
    <br />
    • 来自《罪恶都市传奇》的建筑霓虹灯效
    <br />
    • 最终版改良武器系统
    <br />
    • Xbox版全载具收录
    <br />
    • 新增《圣安地列斯》经典车型（完美适配世界观）
    <br />
    • Xbox版角色与NPC模型（高清纹理重制）
    <br />
    • PS2版原声音乐电台（包含删减的Lionel Richie - Running With The Night单曲）
    <br />
    • 原版风格加载界面与游戏UI（包含100%完成度专属设计）
    <br />
    • 开发团队特别优化的各类修复补丁及隐藏彩蛋
    <br />
    <br />
    REVOLUTION TEAM核心成员：
    <br />
    - LaV07
    <br />
    - Derial Brown
    <br />
    - AndrewMulti
    <br />
    - Hot Dam
    <br />
    免责声明：本模组完全免费且无任何商业用途，由粉丝为爱发电制作完成。Revolution Team向原版游戏开发者致以崇高敬意。由于属于粉丝自制模组，游戏过程中可能出现BUG或崩溃情况，敬请谅解。
</p>
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
