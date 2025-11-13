import streamlit as st
import random
import time

# 页面配置
st.set_page_config(
    page_title="祝福弹窗",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 淡蓝清新背景样式（治愈系）
st.markdown("""
<style>
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    .stApp {
        background: linear-gradient(135deg, #e6f7ff, #c9e6ff); /* 淡蓝渐变背景 */
        padding: 0 !important;
        margin: 0 !important;
    }
    html, body {
        height: 100%;
        overflow: hidden;
    }
    /* 按钮样式适配背景 */
    .stButton > button {
        border-radius: 8px !important;
        font-weight: bold !important;
        padding: 12px 0 !important;
        transition: all 0.3s ease !important;
    }
    .stButton > button:first-child {
        background-color: #67c23a !important; /* 清新绿色开始按钮 */
        color: white !important;
        box-shadow: 0 2px 8px rgba(103, 194, 58, 0.3) !important;
    }
    .stButton > button:first-child:hover {
        background-color: #52c41a !important;
        transform: translateY(-2px) !important;
    }
    .stButton > button:last-child {
        background-color: #fff !important; /* 白色重置按钮 */
        color: #409eff !important;
        border: 1px solid #b3d8ff !important;
        box-shadow: 0 2px 8px rgba(64, 158, 255, 0.1) !important;
    }
    .stButton > button:last-child:hover {
        background-color: #f0f7ff !important;
        transform: translateY(-2px) !important;
    }
    /* 礼物图案样式 */
    .gift-icon {
        text-align: center;
        font-size: 36px;
        margin-bottom: 15px;
        animation: float 3s ease-in-out infinite;
    }
    @keyframes float {
        0% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
        100% { transform: translateY(0px); }
    }
</style>
""", unsafe_allow_html=True)

# 祝福文本库
POPUP_TEXTS = [
    "平安喜乐", "事事如意", "注意身体", "快快乐乐",
    "健康平安", "万事如意", "笑口常开", "前程似锦",
    "考研上岸", "考公上岸", "暴富", "好运连连",
    "心想事成", "一帆风顺", "阖家幸福", "发财",
    "天天开心", "顺利平安", "美梦成真", "活力满满"
]

# 渐变色样式库（与淡蓝背景协调）
GRADIENT_STYLES = [
    "linear-gradient(90deg, #FF9A9E 0%, #FAD0C4 100%)",
    "linear-gradient(90deg, #84FAB0 0%, #8FD3F4 100%)",
    "linear-gradient(90deg, #D4FC79 0%, #96E6A1 100%)",
    "linear-gradient(90deg, #FFECD2 0%, #FCB69F 100%)",
    "linear-gradient(90deg, #E0C3FC 0%, #8EC5FC 100%)",
    "linear-gradient(90deg, #FFDEE9 0%, #B5FFFC 100%)"
]

# 装饰符号库
DECORATIONS = ["★", "☆", "♡", "♢", "♧", "♤", "◆", "◇", "❀", "✦"]

# 初始化会话状态
if "state" not in st.session_state:
    st.session_state.state = {
        "is_started": False,    # 是否开始生成弹窗
        "current_count": 0,     # 当前弹窗数量
        "max_count": 150,       # 铺满屏幕的最大数量
        "interval": 0.2         # 弹窗生成间隔（秒）
    }

# 重置功能
def reset_all():
    st.session_state.state = {
        "is_started": False,
        "current_count": 0,
        "max_count": 150,
        "interval": 0.2
    }

# 初始页面（显示按钮和礼物图案）
if not st.session_state.state["is_started"]:
    # 按钮居中布局
    col_center = st.columns([1, 2, 1])[1]
    with col_center:
        # 增加垂直间距，让元素居中更协调
        st.markdown("""
            <div style="margin-top: 32vh;"></div>
        """, unsafe_allow_html=True)
        
        # 礼物图案（位于开始按钮上方）
        st.markdown('<div class="gift-icon">🎁</div>', unsafe_allow_html=True)
        
        # 开始按钮
        if st.button("✨ 开始", use_container_width=True):
            st.session_state.state["is_started"] = True
            st.rerun()
        
        # 重置按钮
        if st.button("🔄 重置", use_container_width=True):
            reset_all()
            st.rerun()

# 弹窗生成逻辑
if st.session_state.state["is_started"]:
    # 渲染已生成的所有弹窗
    for i in range(st.session_state.state["current_count"]):
        # 固定随机种子，确保弹窗属性稳定
        random.seed(i)
        text = random.choice(POPUP_TEXTS)
        gradient = random.choice(GRADIENT_STYLES)
        decor = random.choice(DECORATIONS)
        
        # 随机尺寸（小型长条）
        width = random.randint(120, 250)
        height = random.randint(40, 70)
        
        # 随机位置（覆盖全屏）
        top = random.randint(3, 97)
        left = random.randint(3, 97)
        
        # 随机旋转角度（轻微倾斜）
        rotate = random.randint(-5, 5)
        
        # 随机层级（控制覆盖关系）
        z_index = i % 10
        
        # 文字颜色适配背景
        text_color = "black" if gradient in [
            "linear-gradient(90deg, #D4FC79 0%, #96E6A1 100%)",
            "linear-gradient(90deg, #FFECD2 0%, #FCB69F 100%)"
        ] else "white"

        # 文字和装饰大小适配
        text_size = random.randint(16, 20)
        decor_size = text_size - 3

        # 弹窗HTML（带淡入动画）
        st.markdown(f"""
        <style>
            @keyframes popUp_{i} {{
                0% {{ opacity: 0; transform: translate(-50%, -50%) rotate({rotate}deg) scale(0.6); }}
                100% {{ opacity: 1; transform: translate(-50%, -50%) rotate({rotate}deg) scale(1); }}
            }}
            .popup_{i} {{
                position: absolute;
                top: {top}%;
                left: {left}%;
                width: {width}px;
                height: {height}px;
                background: {gradient};
                border-radius: 6px;
                box-shadow: 0 2px 8px rgba(0,0,0,0.15);
                z-index: {z_index};
                transform: translate(-50%, -50%) rotate({rotate}deg);
                animation: popUp_{i} 0.4s ease-out forwards;
                display: flex;
                align-items: center;
                justify-content: center;
                gap: 8px;
                padding: 0 12px;
            }}
        </style>
        <div class="popup_{i}" style="color: {text_color}">
            <span style="font-size: {decor_size}px;">{decor}</span>
            <div style="font-size: {text_size}px; font-weight: bold; font-family: 'Microsoft YaHei', sans-serif;">{text}</div>
            <span style="font-size: {decor_size}px;">{decor}</span>
        </div>
        """, unsafe_allow_html=True)

    # 继续生成下一个弹窗
    if st.session_state.state["current_count"] < st.session_state.state["max_count"]:
        time.sleep(st.session_state.state["interval"])
        st.session_state.state["current_count"] += 1
        st.rerun()
    else:
        # 完成提示（与背景协调的样式）
        st.markdown("""
        <div style="position: fixed; top: 20px; left: 50%; transform: translateX(-50%); 
                    background: rgba(255,255,255,0.8); color: #1890ff; padding: 10px 20px; 
                    border-radius: 20px; z-index: 9999; box-shadow: 0 2px 10px rgba(64,158,255,0.2);">
            已铺满屏幕
        </div>
        """, unsafe_allow_html=True)
        
        # 底部重置按钮（与背景协调）
        st.markdown("""
        <div style="position: fixed; bottom: 30px; left: 50%; transform: translateX(-50%); z-index: 9999;">
            <button onclick="window.location.reload()" 
                    style="background-color: #fff; color: #409eff; border: 1px solid #b3d8ff; 
                           padding: 12px 30px; border-radius: 8px; 
                           font-size: 16px; cursor: pointer; font-weight: bold;
                           box-shadow: 0 2px 8px rgba(64,158,255,0.1);">
                🔄 重新开始
            </button>
        </div>
        """, unsafe_allow_html=True)