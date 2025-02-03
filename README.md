# 罪恶都市次世代版中文启动器
> 使用Python+Vue3构建

## 快速开始

### 安装依赖

#### Python

```python
pip install pyinstaller
```

#### Vue
```vue
cd Frontend
npm i
npm i -D vuetify vite-plugin-vuetify
npm i @mdi/font
```

### 构建启动器
#### Python
```python
pyinstaller build.spec
```
#### Vue
```vue
npm run build
```
> 将构建好的dist文件夹替换掉Assets/UI文件夹即可更新前端