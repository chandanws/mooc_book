import numpy as np
import unittest

class JobSchedule:
	"""
	greedy algorithm that schedules jobs in decreasing order of ratio (weight/length)
	"""
	def __init__(self):
		self.job_num = 0 # the number of jobs
		self.job_weight = []
		self.job_length = []
		self.schedule_time = None
		self.order = None # the ordering of jobs

	def buildjobs(self, textfile):
		"""
		build jobs from a text file

		The file describes a set of jobs with positive and integral weights and lengths.
		It has the format
		[number_of_jobs]
		[job_1_weight] [job_1_length]

		"""
		count = 0
		with open(textfile) as infile:
			for line in infile.readlines():
				line = line.strip('\n')
				if count == 0:
					self.job_num = int(line)
				else:
					job_weight, job_length = (int(num) for num in line.split())
					self.job_weight.append(job_weight)
					self.job_length.append(job_length)
				count += 1

		if count-1 != self.job_num:
			raise ValueError

	def scheduling(self):
		"""
		return the sum of weighted completion times of the resulting schedule
		"""
		# ratios of weight and length for every job
		ratios = [self.job_weight[i]/self.job_length[i] for i in range(self.job_num)]
		self.order = np.lexsort((self.job_length, ratios))
		self.order=self.order[::-1]
		print([ (self.job_weight[i], self.job_length[i],self.job_weight[i]/self.job_length[i]) for i in self.order])
		# calculating the sum of weighted completion times of the resulting schedule
		count = 0
		job_length = 0
		for job_ind in self.order:
			job_length = job_length + self.job_length[job_ind]
			count += self.job_weight[job_ind]*job_length
		self.schedule_time = count
		return self.schedule_time


class TestJobSchedule(unittest.TestCase):

	def testcase1(self):
		jobs_to_schedule = JobSchedule()
		jobs_to_schedule.buildjobs('testcase1.txt')
		assert jobs_to_schedule.scheduling() == 16

	def testcase2(self):
		jobs_to_schedule = JobSchedule()
		jobs_to_schedule.buildjobs('testcase2.txt')
		assert jobs_to_schedule.scheduling() == 67247


if __name__ == "__main__":
	unittest.main()







