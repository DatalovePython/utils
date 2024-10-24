

"""
Anger over AI's role in exacerbating inequality (加剧不平等) could endanger the technology's future.

In her new book Cogs and Monsters: What Economics Is, and What It Should Be, Diane Coyle, an economist at Cambridge
University, argues that the digital economy requires new ways of thinking about progress.
“Whatever we mean by the economy growing, by things getting better, the gains will have to be more evenly shared than
in the recent past,” she writes. “An economy of tech millionaires (科技百万富翁) or billionaires (亿万富翁) and gig workers
(零工工作者), with middle-income jobs undercut by automation (自动化削弱), will not be politically（政治上） sustainable（稳定的）.”
Improving living standards and increasing prosperity（兴旺） for more people will require greater use of digital technologies
to boost（促进） productivity in various sectors（各领域）, including health care and construction, says Coyle. But people can’t be
expected to embrace（拥抱） the changes if they’re not seeing the benefits—if they’re just seeing good jobs being destroyed.
In a recent interview with MIT Technology Review, Coyle said she fears that tech’s inequality problem could be a
roadblock (障碍) to deploying (部署) AI. “We’re talking about disruption (颠覆),” she says. “These are transformative（变革型）
technologies that change the ways we spend our time every day, that change business models that succeed.” To make such
“tremendous changes (巨大变革),” she adds, “you need social buy-in (社会认同).”
Instead, says Coyle, resentment (怨恨) is simmering (酝酿) among many as the benefits are perceived to go to elites (精英) in
a handful of prosperous（繁荣） cities.
In the US, for instance, during much of the 20th century the various regions of the country were—in the language of
economists—“converging (趋同),” and financial（经济） disparities (差异) decreased. Then, in the 1980s, came the onslaught (冲击) of
digital technologies, and the trend reversed（反转） itself. Automation wiped out many manufacturing (制造业) and retail (零售业)
jobs. New, well-paying tech jobs were clustered (聚集) in a few cities.
The dominance (主导地位) of a few cities in the invention and commercialization (商业化) of AI means that geographical
disparities in wealth will continue to soar (飙升). Not only will this foster(促进） political and social unrest (动荡), but it
could, as Coyle suggests, hold back the sorts of AI technologies needed for regional economies to grow.
Part of the solution could lie in（在于） somehow loosening the stranglehold (扼制) that Big Tech has on defining the AI agenda（议程）.
That will likely take increased federal funding for research independent of the tech giants（巨头）. Muro and others have
suggested hefty (巨额的) federal funding to help create US regional innovation（创新） centers, for example.

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



"""
One of the biggest challenges in keeping unsafe aging drivers (老年驾驶员) off the road is convincing them that it’s time to turn
over the keys.

“It’s a complete life-changer” when someone stops — or is forced to stop — driving, said Anne M. Menke, a former risk
manager for the Ophthalmic Mutual Insurance Co. (眼科互助保险公司).

Part of the problem in keeping older drivers safe is that the difficulties are addressed piecemeal (零碎地) by different
professions with different focuses, including gerontologists (老年学家), highway administration officials, automotive engineers (汽车工程师)
and others, said Elizabeth Dugan, an associate professor of gerontology at the University of Massachusetts. “There’s
not a National Institute of Older Driver Studies,” she said. “We need better evidence on what makes drivers unsafe” and
what can help, said Dugan, who has written extensively（广泛的） about healthy aging for Consumer Reports and other organizations.

One thing that does seem to work is requiring drivers to report in person for license renewal. Mandatory (强制的) in-person
renewal was associated with a 31 percent reduction in fatal crashes involving drivers 85 or older, according to one
study. Passing vision tests also produced a similar decline in fatal crashes for those drivers, although there appeared
to be no benefit from combining the two.

Many older drivers don’t see eye doctors or can’t afford to. Primary(初级的，主要的） care providers（保健者） have their hands full and may not
be able to follow through（坚持到底） with patients who have trouble driving because they can’t turn their heads or remember where
they are going — or have gotten shorter and haven’t changed their seat settings sufficiently to reach car pedals easily.

As long as（只要） there are other cars on the roads, self-driving cars won’t solve the problems of crashes, said Dugan.
Avoiding dangers posed by all those human drivers would require too many algorithms (算法), she said. But we need to do more
to improve safety, said Dugan.

“If we’re going to have 100-year lives, we need cars that a 90-year-old can drive comfortably.”
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










"""

If you look at the apps on your phone, chances are you have at least one related to your health—and probably several.
Whether it is a mental (心理的) health app, a fitness (健身的) tracker, a connected health device or something else, many of us are
taking advantage of this technology to keep better track of our health in some shape or form. Recent research from the
Organization for the Review of Care and Health Applications found that 350,000 health apps were available on the
market, 90,000 of which launched in 2020 alone.
While these apps have a great deal to offer, it is not always clear how the personal information we input (输入) is collected,
safeguarded (保护) and shared online. Existing（现有的） health privacy law, such as the Health Insurance Portability and Accountability
Act, is primarily focused on the way hospitals, doctors’ offices, clinics（诊所） and insurance companies store health records
online. The health information these apps and health data tracking wearables (可穿戴设备) are collecting typically does not receive
the same legal protections.
Without additional protections in place, companies may share (and potentially monetize) personal health information in
a way consumers may not have authorized or anticipated. In 2021, Flo Health faced a Federal Trade Commission（FTC）
investigation (调查). The FTC alleged (指控) in a complaint（投诉） that "despite（尽管） express privacy claims, the company took control of users'
sensitivity fertility (生育) data and shared it with third parties.” Flo Health and the FTC settled the matter with a Consent
Order requiring the company to get app users' express affirmative（肯定，同意） consent（同意） before sharing their health information as
well as（和...一样） to instruct the third parties to delete the data they had obtained.
Section 5 of the FTC Act empowers the FTC to initiate (启动) enforcement action against unfair or deceptive acts, meaning the
FTC can only act after the fact if a company's privacy practices are misleading or cause unjustified consumer harm.
While the FTC is doing what it can to ensure apps are keeping their promises to consumers around the handling of their
sensitive health information, the rate at which these health apps are hitting the market demonstrates just how
immense (巨大的) of a challenge this is.
As to the prospects (前景) for federal(联邦) legislation(法律), commentators(评论家) suggest that comprehensive(全面) federal privacy legislation seems
unlikely in the short term. States have begun implementing their own solutions to shore up(支撑) protections for
consumer-generated health data. California has been at the forefront of state privacy efforts with the California
Consumer Privacy Act of 2018. Virginia，Colorado and Utah have also recently passed state consumer data privacy
legislation.



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





"""
High school students eager(渴望的) to stand out in the college application process often participate(参加) in a litany (大量的) of
extracurricular (课外的) activities hoping to bolster (增强) their chances of admission to a selective undergraduate(本科) institution(机构).
However, college admissions experts say that the quality of a college hopeful's extracurricular activities matters(质量) more
than the number of activities he or she participates in.
Sue Rexford, the director of college guidance at the Charles E. Smith Jewish Day School, says it is not necessary for
a student filling out the Common Application to list 10 activities in the application.
"No college will expect that a student has a huge laundry list(一长串清单) of extracurriculars that they have been passionately
involved in each for an extended(扩展） period of time," Rexford wrote in an email.
Experts say it is tougher to distinguish (区分) oneself in a school-affiliated（学校附属） extracurricular activity that is common among
high school students than it is to stand out while doing an uncommon activity.
"The competition to stand out and make an impact is going to be much stiffer (更激烈的), and so if they're going to do a popular
activity, I'd say, be the best at it," says Sara Harberson, a college admission consultant.
High school students who have an impressive personal project they are working on independently often impress colleges,
experts say.
"For example, a student with an interest in entrepreneurship (创业) could demonstrate skills and potential by starting a
profitable small business," Olivia Valdes, the founder of Zen Admissions consulting firm, wrote in an email.
Joseph Adegboyega-Edun, a Maryland high school guidance counselor, says unconventional extracurricular activities can
help students impress college admissions offices, assuming they demonstrate serious commitment. "Again, since one of
the big questions high school seniors must consider is 'What makes you unique?', having an uncommon extracurricular
activity vs. a conventional one is an advantage," he wrote in an email.
Experts say demonstrating talent in at least one extracurricular activity can help in the college admissions process,
especially at top-tier (顶级的) undergraduate institutions.
"Distinguishing yourself in one focused type of extracurricular activity can be a positive in the admissions process,
especially for highly selective institutions, where having top grades and test scores is not enough," Katie Kelley,
an admissions counselor at IvyWise admissions consultancy, wrote in an email. "Students need to have that quality or hook
that will appeal to admissions officers and allow them to visualize how the student might come and enrich their campus
community."
Extracurricular activities related to the college major declared on a college application are beneficial (有益的), experts
suggest. "If you already know your major, having an extracurricular that fits into that major can be a big plus," says
Mayghin Levine, the manager of educational opportunities with The Cabbage Patch Settlement House, a Louisville,
Kentucky, nonprofit community center.
High school students who have had a strong positive influence on their community through an extracurricular activity
may impress a college and win a scholarship, says Erica Gwyn, a former math and science magnet program assistant at a
public high school who is now executive director of the Kaleidoscope Careers Academy in Atlanta, a nonprofit
organization.



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







"""
With the smell of coffee and fresh bread floating in the air, stalls(货摊) bursting（充满） with colorful vegetables and tempting (诱人的)
cheeses, and the buzz（翁翁声） of friendly chats, farmers’ markets are a feast (盛宴) for the senses（感官）. They also provide an opportunity
to talk to the people responsible for growing or raising your food, support your local economy (经济) and pick up fresh
seasonal produce (农产品)—all at the same time.
Farmers’ markets are usually weekly or monthly events（每周或每月的活动）, most often with outdoor stalls, which allow farmers or
producers to sell their food directly to customers. The size or regularity (规律性) of markets can vary（变化） from season to season,
depending on the area’s agricultural (农业的) calendar, and you’re likely to find different produce on sale at different times
of the year. By cutting out the middlemen（中间商）, the farmers secure（保护，取得） more profit for their produce. Shoppers also benefit from
seeing exactly where—and to whom—their money is going.
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




