# HappyPandaX_PluginMetadata_TagViaFilename

同 [BaG-Ray/Lanraragi_PluginMetadata_TagViaFilename](https://github.com/BaG-Ray/Lanraragi_PluginMetadata_TagViaFilename) 一致，压缩包的命名方式为gID-gToken-名字.zip。  
Tag加上了汉化，因此需要在根目录(/data)下放置db.text.json文件，但是画师和社团的汉化一直报错，HPX的报错也看不到。不过这点我也不是很需要。  
使用方式为，在关HPX的情况下，将整个文件夹放到HPX的根目录(/data)下，然后开启再去设置的插件下安装就行。  

但是，HPX和Lanraragi有很大不同，HPX的元数据获取后，不会把原来的替换掉，包括标题也不会换掉。这点远远不如Lanraragi，不过这UI确实好看。这个问题我看了整个插件的代码，感觉应该不是这里控制的，应该是HPX那边的逻辑有问题。
