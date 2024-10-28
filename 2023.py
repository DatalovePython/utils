
"""
In the quest for the perfect lawn (草坪), homeowners across the country are taking a shortcut (捷径)—and it is the
environment (环境) that is paying the price. About eight million square metres of plastic (塑料) grass is sold each year
but opposition (反对) has now spread to the highest gardening (园艺) circles. The Chelsea Flower Show (切尔西花展) has banned
fake (假) grass from this year’s event, declaring (声明) it to be not part of its ethos (道德理念). The Royal Horticultural
Society (RHS) (皇家园艺学会), which runs the annual (年度的) show in west London, says it has introduced the ban because of the
damage (破坏) plastic grass does to the environment and biodiversity (生物多样性).
Ed Horne, of the RHS, said: “We launched our sustainability (可持续性) strategy (策略) last year and fake grass is just not
in line with our ethos and views on plastic. We recommend using real grass because of its environmental benefits, which
include supporting wildlife (野生动物), alleviating (缓解) flooding (洪水) and cooling the environment.”
The RHS’s decision comes as campaigners (倡导者) try to raise awareness (意识) of the problems fake grass causes. A Twitter
account, which claims to “cut through the greenwash (漂绿现象)” of artificial (人工的) grass, already has more than 20,000
followers (关注者). It is trying to encourage people to sign two petitions (请愿书), one calling for a ban on the sale of
plastic grass and another calling for an “ecological (生态) damage” tax on such lawns. They have gathered (收集) 7,276 and
11,282 signatures (签名).
However, supporters (支持者) of fake grass point out that there is also an environmental impact (影响) with natural lawns,
which need mowing (修剪) and therefore usually consume electricity (电) or petrol (汽油). The industry also points out that
real grass requires considerable (相当大的) amounts of water, weed killer (除草剂) or other treatments (处理), and that people
who lay (铺设) fake grass tend to use their garden more. The industry also claims that people who lay fake grass spend an
average (平均) of £500 on trees or shrubs (灌木) for their garden, which provides habitat (栖息地) for insects (昆虫).
In response (回应) to another petition last year about banning fake lawns, which gathered 30,000 signatures, the
government responded that it has “no plans to ban the use of artificial grass.”
It added: “We prefer to help people and organizations (组织) make the right choice rather than legislating (立法) on such
matters. However, the use of artificial grass must comply (符合) with the legal and policy (政策) safeguards (保障措施) in
place to protect biodiversity and ensure sustainable (可持续的) drainage (排水), while measures such as the strengthened
biodiversity duty should serve to encourage public authorities (公共当局) to consider sustainable alternatives.”

"""










class HAManagerInterface:
    """高可用管理抽象类"""
    __metaclass__ = ABCMeta

    @abstractmethod
    def init_ha_env(self, ha_subnet, node_ip, node_name,
                    bind_link, product_type):
        """
        初始化高可用环境，需要创建私网、加载镜像和swarm 初始化
        :param ha_subnet: swarm内网地址
        :param node_ip: 节点ip
        :param node_name: 节点名
        :param bind_link: swarm绑定链路
        :param product_type: 产品类型
        :return:
        """

    @abstractmethod
    def clear_ha_env(self):
        """
        清理节点环境
        :return:
        """

    @abstractmethod
    def add_node(self, node_id, node_ip, role, net_card):
        """
        添加节点
        :param node_id: 目标节点的id(hostname)
        :param node_ip: 目标节点ip
        :param role: 目标节点的角色
        :param net_card: 目标节点绑定的网卡
        :return:
        """











"""
It’s easy to dismiss (否定) as absurd (荒谬的) the federal (联邦的) government’s ideas for plugging (填补) the chronic (长期的)
funding gap (资金缺口) of our national parks (国家公园). Can anyone really think it’s a good idea to allow Amazon deliveries
(派送) to your tent in Yosemite (优胜美地) or food trucks (餐车) to line up under the redwood trees (红杉树) at Sequoia National
Park (红杉国家公园)?
But the administration (政府) is right about one thing: U.S. national parks are in crisis (危机). Collectively (总体来说), they
have a maintenance backlog (维修积压) of more than $12 billion. Roads (道路), trails (小径), restrooms (卫生间), visitor centers
(游客中心) and other infrastructure (基础设施) are crumbling (破损).
But privatizing (私有化) and commercializing (商业化) the campgrounds (露营地) would not be the panacea (灵丹妙药) that the Interior
Department’s (内政部) Outdoor Advisory Committee (户外咨询委员会) would have us believe. Campgrounds are a tiny portion (小部分) of
the overall infrastructure backlog, and concessionaires (特许经营商) in the parks hand over, on average (平均), only about 5%
of their revenues (收入) to the National Park Service (国家公园管理局).
Moreover (此外), increased privatization would certainly undercut (削弱) one of the major reasons (主要原因) why 300 million
visitors come to the parks each year: to enjoy nature (享受自然) and get a respite (休息) from the commercial drumbeat
(商业的鼓噪) that overwhelms (淹没) daily life.
The real problem is that the parks have been chronically starved (长期匮乏) of funding. We conducted a comprehensive (全面的)
survey (调查) examining how U.S. residents view their national parks, and we found that Americans place a very high value
(重视) on them—whether or not they actually visit them. The peer-reviewed (同行评审的) economic survey of 700 U.S. taxpayers
(纳税人), conducted by mail and internet, also found that people would be willing to pay a significant (可观的) amount of
money to make sure the parks and their programs are kept intact (完好无损). Some 81% of respondents (受访者) said they would
be willing to pay additional taxes (额外税款) for the next 10 years to avoid any cuts to the national parks.
The national parks provide great value to U.S. residents both as places to escape (逃离) and as symbols (象征) of nature.
On top of this, they produce value from their extensive (广泛的) educational programs (教育项目), their positive impact (积极影响)
on the climate (气候) through carbon sequestration (碳封存), their contribution (贡献) to our cultural (文化的) and artistic
(艺术的) life, and of course through tourism (旅游).
The parks also help keep America’s past alive, working with thousands of local jurisdictions (地方司法管辖区) around the
country to protect historical sites (历史遗址)—including Ellis Island (埃利斯岛) and Gettysburg (葛底斯堡)—and to bring the stories
of these places to life. The parks do all this on a shoestring (极少的资金). Congress (国会) allocates (拨款) only $3 billion a
year to the national park system—an amount that has been flat (持平) since 2001 (in inflation-adjusted dollars) with the
exception (例外) of a onetime (一次性的) boost in 2009 as part of the Obama stimulus package (刺激方案). Meanwhile (同时), the
number of annual visitors has increased by more than 50% since 1980, and now stands at 330 million visitors per year.

"""







class HAManagerInterface:
    """高可用管理抽象类"""
    __metaclass__ = ABCMeta

    @abstractmethod
    def init_ha_env(self, ha_subnet, node_ip, node_name,
                    bind_link, product_type):
        """
        初始化高可用环境，需要创建私网、加载镜像和swarm 初始化
        :param ha_subnet: swarm内网地址
        :param node_ip: 节点ip
        :param node_name: 节点名
        :param bind_link: swarm绑定链路
        :param product_type: 产品类型
        :return:
        """

    @abstractmethod
    def clear_ha_env(self):
        """
        清理节点环境
        :return:
        """

    @abstractmethod
    def add_node(self, node_id, node_ip, role, net_card):
        """
        添加节点
        :param node_id: 目标节点的id(hostname)
        :param node_ip: 目标节点ip
        :param role: 目标节点的角色
        :param net_card: 目标节点绑定的网卡
        :return:
        """









"""
The Internet may be changing merely what we remember, not our capacity (能力) to do so, suggests Columbia University
psychology (心理学) professor Betsy Sparrow. In 2011, Sparrow led a study in which participants (参与者) were asked to record
40 factoids (小知识) in a computer (“an ostrich’s (鸵鸟的) eye is bigger than its brain,” for example). Half of the
participants were told the information would be erased (抹去), while the other half were told it would be saved (保存).
Guess what? The latter (后者) group made no effort (努力) to recall (回忆) the information when quizzed (询问) on it later,
because they knew they could find it on their computers. In the same study, a group was asked to remember both the
information and the folders (文件夹) it was stored in. They didn’t remember the information, but they remembered how to
find the folders. In other words, human memory (记忆) is not deteriorating (退化) but “adapting (适应) to new communications
technology,” Sparrow says.
In a very practical (实用的) way, the Internet is becoming an external (外部的) hard drive (硬盘) for our memories, a process
known as “cognitive offloading (认知卸载).” Traditionally (传统上), this role was fulfilled (完成) by data banks (数据库),
libraries (图书馆), and other humans. Your father may never remember birthdays because your mother does, for instance
(例如). Some worry that this is having a destructive (破坏性的) effect on society (社会), but Sparrow sees an upside (好处).
Perhaps, she suggests, the trend will change our approach (方法) to learning from a focus on individual (个别的) facts and
memorization (记忆) to an emphasis (重点) on more conceptual (概念性的) thinking—something that is not available (可用的) on the
Internet. “I personally (个人) have never seen all that much intellectual (智力的) value in memorizing things,” Sparrow
says, adding that we haven’t lost our ability to do it.
Still other experts say it’s too soon to understand how the Internet affects our brains. There is no experimental (实验的)
evidence (证据) showing that it interferes (干扰) with our ability to focus (集中), for instance, wrote psychologists
Christopher Chabris and Daniel Simons. And surfing the web exercised (锻炼) the brain more than reading did among
computer-savvy (精通计算机的) older adults in a 2008 study involving (涉及) 24 participants at the Semel Institute for
Neuroscience (神经科学) and Human Behavior (人类行为) at the University of California, Los Angeles (加州大学洛杉矶分校).
“There may be costs (代价) associated with our increased (增加的) reliance (依赖) on the Internet, but I’d have to imagine
that the overall (总体的) benefits (好处) are going to outweigh (超过) those costs,” observes psychology professor Benjamin
Storm. “It seems pretty clear that memory is changing, but is it changing for the better? At this point, we don’t know.”



"""







class HAManagerInterface:
    """高可用管理抽象类"""
    __metaclass__ = ABCMeta

    @abstractmethod
    def init_ha_env(self, ha_subnet, node_ip, node_name,
                    bind_link, product_type):
        """
        初始化高可用环境，需要创建私网、加载镜像和swarm 初始化
        :param ha_subnet: swarm内网地址
        :param node_ip: 节点ip
        :param node_name: 节点名
        :param bind_link: swarm绑定链路
        :param product_type: 产品类型
        :return:
        """

    @abstractmethod
    def clear_ha_env(self):
        """
        清理节点环境
        :return:
        """

    @abstractmethod
    def add_node(self, node_id, node_ip, role, net_card):
        """
        添加节点
        :param node_id: 目标节点的id(hostname)
        :param node_ip: 目标节点ip
        :param role: 目标节点的角色
        :param net_card: 目标节点绑定的网卡
        :return:
        """






"""

Teenagers (青少年) are paradoxical (矛盾的). That’s a mild (温和的) and detached (冷静的) way of saying something that parents
often express with considerably (相当) stronger language (语言). But the paradox (矛盾) is scientific (科学的) as well as
personal (个人的). In adolescence (青春期), helpless (无助的) and dependent (依赖的) children who have relied (依靠) on grown-ups for
just about everything become independent (独立的) people who can take care of themselves and help each other. At the same
time, once cheerful (快乐的) and compliant (顺从的) children become rebellious (叛逆的) teenage risk-takers (冒险者), often to the
point of self-destruction (自我毁灭). Accidental (意外的) deaths go up dramatically (显著地) in adolescence.


A new study published (发表) in the journal Child Development (《儿童发展》), by Eveline Crone of the University of London
(伦敦大学) and colleagues (同事), suggests that the positive (积极的) and negative (消极的) sides of teenagers go hand in hand
(齐头并进). The study is part of a new wave (浪潮) of thinking about adolescence. For a long time, scientists (科学家) and
policy makers (政策制定者) concentrated (集中) on the idea that teenagers were a problem that needed to be solved. The new
work emphasizes (强调) that adolescence is a time of opportunity (机遇) as well as risk (风险).


The researchers studied “prosocial” (亲社会的) and rebellious traits (特质) in more than 200 children and young adults,
ranging (范围) from 11 to 28 years old. The participants (参与者) filled out questionnaires (问卷) about how often they did
things that were altruistic (利他的) and positive, like sacrificing (牺牲) their own interests to help a friend, or
rebellious and negative, like getting drunk (喝醉) or staying out late (熬夜).


Other studies have shown that rebellious behavior (叛逆行为) increases as you become a teenager and then fades away (逐渐消失)
as you grow older. But the new study shows that, interestingly (有趣的是), the same pattern (模式) holds for prosocial
behavior. Teenagers were more likely than younger children or adults to report that they did things like unselfishly
(无私地) help a friend.


Most significantly (最显著地), there was a positive correlation (正相关) between prosociality and rebelliousness. The
teenagers who were more rebellious were also more likely to help others. The good and bad sides of adolescence seem to
develop together.


Is there some common factor (因素) that underlies (潜在) these apparently (表面上) contradictory (矛盾的) developments? One idea
is that teenage behavior is related to what researchers call “reward sensitivity” (奖励敏感性). Decision-making (决策) always
involves balancing rewards and risks (风险), benefits (好处) and costs (成本). “Reward sensitivity” measures (衡量) how much
reward it takes to outweigh (超过) risk.


Teenagers are particularly (尤其) sensitive (敏感的) to social rewards—winning (赢得) the game, impressing (给……留下深刻印象) a new
friend, getting that boy to notice (注意) you. Reward sensitivity, like prosocial behavior and risk-taking, seems to go
up in adolescence and then down again as we age. Somehow (不知何故), when you hit 30, the chance that something exciting
(令人兴奋的) and new will happen at that party just doesn’t seem to outweigh the effort (努力) of getting up off the couch.


"""




class HAManagerInterface:
    """高可用管理抽象类"""
    __metaclass__ = ABCMeta

    @abstractmethod
    def init_ha_env(self, ha_subnet, node_ip, node_name,
                    bind_link, product_type):
        """
        初始化高可用环境，需要创建私网、加载镜像和swarm 初始化
        :param ha_subnet: swarm内网地址
        :param node_ip: 节点ip
        :param node_name: 节点名
        :param bind_link: swarm绑定链路
        :param product_type: 产品类型
        :return:
        """

    @abstractmethod
    def clear_ha_env(self):
        """
        清理节点环境
        :return:
        """

    @abstractmethod
    def add_node(self, node_id, node_ip, role, net_card):
        """
        添加节点
        :param node_id: 目标节点的id(hostname)
        :param node_ip: 目标节点ip
        :param role: 目标节点的角色
        :param net_card: 目标节点绑定的网卡
        :return:
        """








"""


New building regulations (建筑法规) aimed at improving energy efficiency (能效) are set to increase the price of new homes,
as well as those of extensions (扩建) and loft conversions (阁楼改造) on existing ones.


The rules, which came into effect (生效) on Wednesday in England, are part of government plans to reduce the UK’s carbon
emissions (碳排放) to net zero (净零) by 2050. They set new standards for ventilation (通风), energy efficiency, and heating
(供暖), and state that new residential buildings (住宅建筑) must have charging points (充电桩) for electric vehicles (电动汽车).


The moves are the most significant (重要的) change to building regulations in years, and industry experts (行业专家) say they
will inevitably (不可避免地) lead to higher prices at a time when a shortage (短缺) of materials (材料) and high labour costs
(高劳动力成本) are already driving up bills (账单).


Brian Berry, chief executive (首席执行官) of the Federation of Master Builders (建筑师联合会), a trade group (行业组织) for small and
medium-sized builders, says the measures (措施) will require new materials, testing methods (测试方法), products, and systems
to be installed. “All this comes at an increased cost (增加的成本) during a time when prices are already sky high (居高不下).
Inevitably, consumers (消费者) will have to pay more,” he says.


Gareth Belsham, of surveyors (测量师) Naismiths, says “people who are upgrading (升级), or extending their home, will be
directly affected. The biggest changes relate to heating and insulation (隔热),” he says. “There are new rules concerning
(关于) the amount of glazing (玻璃安装) used in extensions, and any new windows or doors must be highly insulated.”


Windows and doors will have to adhere to (遵循) higher standards, while there are new limits (限制) on the amount of
glazing you can have to reduce unwanted heat from the sun.


Thomas Goodman, of My Job Quote, a site which sources quotes (报价), says this will bring in new restrictions for
extensions. “Glazing on windows, doors and roof lights (天窗) must cover no more than 25% of the floor area to prevent
heat loss (热量流失),” he says.


As the rules came into effect last Wednesday, property developers (房地产开发商) were rushing to file plans (提交计划) just
before the deadline (截止日期), according to Belsham. Any plans submitted before that date are considered to be under the
previous (之前的) rules, and can go ahead as long as work starts before 15 June next year.


Builders which have costed (估价) projects, but have not filed the paperwork, may need to go back and submit fresh (新的)
estimates (估算), says Marcus Jefford of Build Aviator, which prices projects.


Materials prices are already up 25% in the last two years, according to figures from the Construction Products
Association (建筑产品协会). How much overall prices will increase as a result of the rule changes is not clear. “While
admirable (令人钦佩的) in their intentions, they will add to the cost of housebuilding at a time when many already feel that
they are priced out of (被挤出) homeownership,” says Jonathan Rolande of the National Association of Property Buyers
(全国房地产买家协会). “An average extension will probably see around £3,000 additional (额外的) cost thanks to the new regs (法规).”


John Kelly, a construction lawyer (建筑律师) at Freeths law firm, believes prices will eventually (最终) come down. But not
in the immediate future (近期). “As the marketplace (市场) adapts to the new requirements (要求), and the technologies (技术)
that support them, the scaling up (扩大规模) of these technologies will eventually bring costs down, but in the short term,
we will all have to pay the price of the necessary transition (过渡),” he says.


However, the long-term effects (长期影响) of the changes will be more comfortable (舒适的) and energy-efficient homes, adds
Andrew Mellor. “Homeowners will probably recoup (收回) that cost over time in energy bill savings (节能账单节省). It will
obviously be very volatile (波动的) at the moment, but they will have that benefit (好处) over time.”

"""


class HAManagerInterface:
    """高可用管理抽象类"""
    __metaclass__ = ABCMeta

    @abstractmethod
    def init_ha_env(self, ha_subnet, node_ip, node_name,
                    bind_link, product_type):
        """
        初始化高可用环境，需要创建私网、加载镜像和swarm 初始化
        :param ha_subnet: swarm内网地址
        :param node_ip: 节点ip
        :param node_name: 节点名
        :param bind_link: swarm绑定链路
        :param product_type: 产品类型
        :return:
        """

    @abstractmethod
    def clear_ha_env(self):
        """
        清理节点环境
        :return:
        """

    @abstractmethod
    def add_node(self, node_id, node_ip, role, net_card):
        """
        添加节点
        :param node_id: 目标节点的id(hostname)
        :param node_ip: 目标节点ip
        :param role: 目标节点的角色
        :param net_card: 目标节点绑定的网卡
        :return:
        """




"""

In the late 18th century (十八世纪后期), William Wordsworth (威廉·华兹华斯) became famous (出名) for his poems about nature (自然). And
he was one of the founders (创始人) of a movement called Romanticism (浪漫主义), which celebrated (赞美) the wonders of the
natural world (自然界的奇观).


Poetry (诗歌) is powerful (有力量的). Its energy and rhythm (韵律) can capture (吸引) a reader, transport them to another world
(带到另一个世界) and make them see things differently (以不同方式看待事物). Through carefully selected words and phrases (精心选择的词语和短语),
poems can be dramatic (戏剧性的), funny (有趣的), beautiful (美丽的), moving (感人的) and inspiring (鼓舞人心的).


No one knows for sure (确切地) when poetry began (起源), but it has been around for thousands of years (存在了几千年), even before
people could write (在书写之前). It was a way to tell stories (讲述故事) and pass down history (传递历史). It is closely related
(密切相关) to song (歌曲) and even when written (即使写成文字), it is usually created to be performed out loud (通常是为了大声朗诵). Poems
really come to life (焕发活力) when they are recited (朗诵). This can also help with understanding (理解) them too, because the
rhythm (节奏) and sounds of the words become clearer (更加清晰).


"""


class HAManagerInterface:
    """高可用管理抽象类"""
    __metaclass__ = ABCMeta

    @abstractmethod
    def init_ha_env(self, ha_subnet, node_ip, node_name,
                    bind_link, product_type):
        """
        初始化高可用环境，需要创建私网、加载镜像和swarm 初始化
        :param ha_subnet: swarm内网地址
        :param node_ip: 节点ip
        :param node_name: 节点名
        :param bind_link: swarm绑定链路
        :param product_type: 产品类型
        :return:
        """

    @abstractmethod
    def clear_ha_env(self):
        """
        清理节点环境
        :return:
        """

    @abstractmethod
    def add_node(self, node_id, node_ip, role, net_card):
        """
        添加节点
        :param node_id: 目标节点的id(hostname)
        :param node_ip: 目标节点ip
        :param role: 目标节点的角色
        :param net_card: 目标节点绑定的网卡
        :return:
        """


