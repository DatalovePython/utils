
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

"""
Anger over AI's role in exacerbating inequality (加剧不平等) could endanger the technology's future.
In her new book Cogs and Monsters: What Economics Is, and What It Should Be, Diane Coyle, an economist at Cambridge University, argues that the digital economy requires new ways of thinking about progress.
“Whatever we mean by the economy growing, by things getting better, the gains will have to be more evenly shared than in the recent past,” she writes. “An economy of tech millionaires (科技百万富翁) or billionaires (亿万富翁) and gig workers (零工工作者), with middle-income jobs undercut by automation (自动化削弱), will not be politically sustainable.”
Improving living standards and increasing prosperity for more people will require greater use of digital technologies to boost productivity in various sectors, including health care and construction, says Coyle. But people can’t be expected to embrace the changes if they’re not seeing the benefits—if they’re just seeing good jobs being destroyed.
In a recent interview with MIT Technology Review, Coyle said she fears that tech’s inequality problem could be a roadblock (障碍) to deploying (部署) AI. “We’re talking about disruption (颠覆),” she says. “These are transformative technologies that change the ways we spend our time every day, that change business models that succeed.” To make such “tremendous changes (巨大变革),” she adds, “you need social buy-in (社会认同).”
Instead, says Coyle, resentment (怨恨) is simmering (酝酿) among many as the benefits are perceived to go to elites (精英) in a handful of prosperous cities.
In the US, for instance, during much of the 20th century the various regions of the country were—in the language of economists—“converging (趋同),” and financial disparities (差异) decreased. Then, in the 1980s, came the onslaught (冲击) of digital technologies, and the trend reversed itself. Automation wiped out many manufacturing (制造业) and retail (零售业) jobs. New, well-paying tech jobs were clustered (聚集) in a few cities.
The dominance (主导地位) of a few cities in the invention and commercialization (商业化) of AI means that geographical disparities in wealth will continue to soar (飙升). Not only will this foster political and social unrest (动荡), but it could, as Coyle suggests, hold back the sorts of AI technologies needed for regional economies to grow.
Part of the solution could lie in somehow loosening the stranglehold (扼制) that Big Tech has on defining the AI agenda. That will likely take increased federal funding for research independent of the tech giants. Muro and others have suggested hefty (巨额的) federal funding to help create US regional innovation centers, for example.
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

  
