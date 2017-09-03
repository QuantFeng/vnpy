


def main():
    """主程序入口"""
    # 创建Qt应用对象
    qApp = createQApp()

    # 创建事件引擎
    ee = EventEngine()

    # 创建主引擎
    me = MainEngine(ee)

    # 添加交易接口
    me.addGateway(ctpGateway)
    me.addGateway(oandaGateway)
    me.addGateway(ibGateway)
    me.addGateway(huobiGateway)
    me.addGateway(okcoinGateway)

    if system == 'Windows':
        me.addGateway(femasGateway)
        me.addGateway(xspeedGateway)
        me.addGateway(sgitGateway)
        me.addGateway(shzdGateway)

    # 添加上层应用
    me.addApp(riskManager)
    me.addApp(ctaStrategy)
    me.addApp(spreadTrading)

    # 创建主窗口
    mw = MainWindow(me, ee)
    mw.showMaximized()

    # 在主线程中启动Qt事件循环
    sys.exit(qApp.exec_())


if __name__ == '__main__':
    main()