
#!/usr/bin/env python3
# encoding: utf-8
# author: ninghuxin
# created time: 2023年06月06日 星期一 15时12分41秒

"""
Good morning / afternoon, respected professors.
My name is Lu Zhongchuan, and I’m deeply grateful for this opportunity to introduce myself. 

  I hold a Bachelor’s degree in E - Commerce (Information Management) from Hangzhou Dianzi University Information Engineering School, 

where I graduated with honors, including multiple scholarships and recognition as an Outstanding League Member. 
Currently, I aim to pursue a Master’s in Engineering Management (MEM) to integrate my technical expertise with advanced managerial knowledge, 
becoming a leader in technology - driven organizations.
Academically, my coursework in Management, Statistics, Data Structures, 
and Management Information Systems laid a robust foundation for both technical and analytical thinking.

  I also strengthened my practical skills through certifications like CET - 6 and advanced office software proficiency. 
  These experiences not only sharpened my problem - solving abilities but also sparked
  my interest in bridging technology with systematic management methodologies.
Professionally, I’ve accumulated 7 years of experience in the IT industry.
At Ruijie Networks, a leader in China’s cloud desktop solutions, I served as a Software Development Engineer, 
designing distributed infrastructure modules for their top - ranked VDI / IDV products.
Earlier, at Newland Digital Technology, I contributed to large - scale projects such as the “Beijing Iron Tower Operation System” 
and Fujian’s agricultural cloud platform as a Java Backend Engineer.
These roles taught me to balance technical precision with cross - functional collaboration — skills I aim to refine further through MEM studies.

  Why MEM? While excelling in technical roles, I realized the growing need for managers who understand both 
  engineering complexities and business strategies.
                                                                          
For instance, leading cloud infrastructure development required not just coding skills but also resource allocation and risk management — 
areas where formal training in engineering management would add immense value.

With a preliminary exam score of 188, I’ve demonstrated readiness for rigorous academic challenges.
Looking ahead,
                                                                                                                                                                                                                                                                                                                                                                    I aspire to specialize in Information Engineering Management, focusing on optimizing IT project lifecycles through data - driven decision - making. As a CPC member, I prioritize teamwork and ethical leadership, values I will uphold throughout my studies and career. This MEM program aligns perfectly with my vision to drive innovation at the intersection of technology and management.
Thank you for your consideration. I’m eager to contribute my passion and learn from this esteemed program.

"""


from rccpcangjie.common import constants as const
from rccpcangjie.common.constants import THICK_CSI_STORAGE_CLASS
from rccpcangjie.tasks.task_base import RootTaskBase


_RESIDUAL_CNT = 1


class RecycleDatabaseSnapshotsTask(RootTaskBase):
    """
    snapshot database task
    """

    def __init__(self, task_info):
        super().__init__(task_info)
        self._recycle_threshold = task_info["recycle_threshold"] * const.GB
        self._recycle_percent_threshold = task_info["recycle_percent_threshold"]

    def recycle_database_snapshots(self):
        """
        recycle database snapshots
        """
        storage_type = self._root_mgr.get_database_storage_type()
        if storage_type == THICK_CSI_STORAGE_CLASS:
            stats = self._root_mgr.get_snapshots_stats()
            space_free = stats.capacity - stats.space_used
            free_percent = space_free / stats.capacity
            if space_free < self._recycle_threshold or \
                    free_percent < self._recycle_percent_threshold:
                snapshots = self._root_mgr.get_database_snapshots()
                if len(snapshots) > _RESIDUAL_CNT:
                    self._root_mgr.delete_snapshots(residual_cnt=_RESIDUAL_CNT)
                else:
                    self._root_mgr.delete_snapshots()
