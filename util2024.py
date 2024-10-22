
"""
THE UK is facing a future construction (建造，建筑） crisis (危机） because of a failure to plant trees to produce wood, a trade body has warned.
	Confor chiefs believe urgent action is needed to reduce the country's reliance (依赖）
	 on timber (木材） imports and provide a stable (稳定的） supply of wood for future generations.
	Currently only 20 per cent of the UK's wood requirement is homegrown while it remains the second-largest net importer of timber in the world, bringing in around £7.5 billion annually (每年）.
	Coming at a time of fresh incentives (激励措施） from the UK government for landowners to grow more trees, the trade body says these don't go far enough and fail to promote the benefits of planting them to boost (增加） timber supplies.
	“Not only are we facing a carbon crisis now, but we will also be facing a future construction crisis because of a failure to plant trees to produce wood,"said Stuart Goodall, chief executive (首席执行官） of Confor."For decades we have not taken responsibility for investing in our domestic (国内的） wood supply, leaving us exposed (暴露） to fluctuating (波动的） prices and fighting for future supplies of wood as global demand rises and our own supplies fall."
	The UK has ideal conditions for growing wood to build low-carbon homes and is a global leader in certifying (证明） that its forests are sustainably (可持续地） managed, Confor say. While around three quarters of Scottish homes are built from Scottish timber, the use of home-grown wood in England is only around 25 per cent.
	The causes of the UK’s current position are complex and range from outdated (过时的） perceptions (观念） of productive forestry to the decimation (大量毁灭） of trees from grey squirrels. It also encompasses (包含） significant (重大的） hesitation (犹豫） on behalf of farmers and other landowners to invest in longer term planting projects.
	While productive tree planting can deliver real financial benefits to rural economies and contribute to the UK’s net zero strategy, the focus of government support continues to be on food production and the rewilding (再野生化） and planting of native woodland solely (仅仅） for biodiversity.
	The recently launched Woodland Creation Offer, which pledges (承诺） farmers and landowners £10,000 for each hectare planted, failed to mention timber production, albeit (尽管） the Forestry Commission's Richard Stanford has since spoken of the importance of it.
	Stuart added: "While food production and biodiversity health are clearly of critical (关键的） importance, we need our land to also provide secure (可靠的） supplies of wood for construction, manufacturing and to contribute to net zero.
	“While the UK government has stated its ambition (雄心） for more tree planting, there has been little action on the ground. Confor is now calling for much greater impetus (推动力） behind those aspirations (愿望） to ensure we have enough wood to meet increasing demand.”

"""



@check_retry_desired(attempts=3, interval=30, desired_result=False)
def _is_mangle_prerouting_useless(self):
    """
    判断 mangle prerouting 链中无用 的entry
    预期删除所有来重建
    :return:
    """
    table = ManglePreRoutingTable(self.sbox_path)
    for port_info in self.port_info:
        entrys = table.entrys(filter_dict={
            "protocol": port_info['Protocol'],
            "port": port_info['PublishedPort']
        })

        for entry in entrys:
            if entry.markset != self.markset:
                logger.warning("%s may exist useless prerouting ,"
                            " expect markset %s ,actual %s",
                            self.svc.name, self.markset, entry)
                return True
    return False

  
