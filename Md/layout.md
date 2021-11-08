#关于项目布局设置：

最小控件是ZButton，几个ZButton组成一个ZGroup，几个ZGroup排列成一个ZGroupList
ZGroup中采用表格布局，  
ZButton中的尺寸规则为Preferred。类型：小-1\*1，中2\*2，大4\*4，高2\*4，宽4\*2  
ZButton的高度采用动态计算，当其尺寸发生改变后，采用事件过滤器修改其高度。
ZButton放置从第一行，第0列开始，（第0行放空白的label用于占位


截至目前，ZGroup中的布局设计完成
