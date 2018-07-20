work_load = 15 #hours 
study_load = 45 #hours 
exercise_load = 5 #hours 
sleep_need = 6.5 #hours
days_off = 1 #days
semester_duration = 13 #weeks
semester_working_days = semester_duration*7 #days

class CourseClass:
	""""default class with attributes""" 
	def __init__(self,classes_per_week,hours_per_class,hours_processing_each_class,hours_memorizing_each_class,review_amount):
		self.classes_per_week = classes_per_week
		self.hours_per_class = hours_per_class
		self.hours_processing_each_class = hours_processing_each_class
		self.hours_memorizing_each_class = hours_memorizing_each_class
		self.review_amount = review_amount
		self.reviewing_time = self.review_amount*self.hours_memorizing_each_class*(1/3)  
		self.hours_weekly = round(self.classes_per_week*(self.hours_per_class + self.hours_processing_each_class + self.hours_memorizing_each_class + self.review_amount))



class CourseMaterial:
	def __init__(self,page_amount,pages_per_hour_reading,pages_per_hour_memorizing,review_amount):
		self.page_amount = page_amount
		self.pages_per_hour_reading = pages_per_hour_reading
		self.pages_per_hour_memorizing = pages_per_hour_memorizing
		self.review_amount = review_amount
		self.reading_time = self.page_amount/self.pages_per_hour_reading
		self.memorizing_time = self.page_amount/self.pages_per_hour_memorizing
		self.reviewing_time = self.review_amount*self.memorizing_time*(1/3)
		self.hours_needed = round(self.reading_time + self.memorizing_time + self.reviewing_time)


def apply_20_80(thing, hours_needed):
	reduction_factor = 0.4
	print("Go and figure out how to do the 80% most important stuff of {} in {} hours. Good luck!".format(thing, round(hours_needed*reduction_factor)))
	return hours_needed*reduction_factor

def important_reminder():
	print("Remeber! If you feel like you're spinning your wheels, you're wasting your time.\n Progress with the maximum yield stuff or go do something fun.")


def main():
	if __name__ == "__main__":

		celbio1 = CourseClass(
			classes_per_week=3,
			hours_per_class= 1.75,
			hours_processing_each_class= 1,
			hours_memorizing_each_class= 1,
			review_amount=2)

		celbio2 = CourseClass(
			classes_per_week=3,
			hours_per_class= 1.75,
			hours_processing_each_class= 1,
			hours_memorizing_each_class= 1,
			review_amount=2)

		anatomie= CourseClass(
			classes_per_week=1,
			hours_per_class= 2.5,
			hours_processing_each_class= 1.5,
			hours_memorizing_each_class= 1,
			review_amount=3)

		wissenshaft = CourseClass(
			classes_per_week=1,
			hours_per_class= 1.5,
			hours_processing_each_class= 0.5,
			hours_memorizing_each_class= 0.5,
			review_amount=2)

		filosofie = CourseClass(
			classes_per_week=1,
			hours_per_class= 2,
			hours_processing_each_class= 1,
			hours_memorizing_each_class= 1,
			review_amount=1)

		celbio_book = CourseMaterial(page_amount= 250,
			pages_per_hour_reading= 15,
			pages_per_hour_memorizing= 5,
			review_amount =2)

		anatomy_book = CourseMaterial(page_amount= 800,
			pages_per_hour_reading= 30,
			pages_per_hour_memorizing= 5,
			review_amount =4)

		philosophy_book = CourseMaterial(page_amount= 100,
			pages_per_hour_reading= 20,
			pages_per_hour_memorizing= 4,
			review_amount =1)

		wissenshaft_slides = CourseMaterial(page_amount= 450,
			pages_per_hour_reading= 100,
			pages_per_hour_memorizing= 40,
			review_amount =1) 



		weekly_load = celbio1.hours_weekly + celbio2.hours_weekly + anatomie.hours_weekly + wissenshaft.hours_weekly + filosofie.hours_weekly + celbio_book.hours_needed/semester_duration + anatomy_book.hours_needed/semester_duration + philosophy_book.hours_needed/semester_duration + wissenshaft_slides.hours_needed/semester_duration

		print("celbio1: {} hours weekly".format(celbio1.hours_weekly))
		print("celbio2: {} hours weekly".format(celbio2.hours_weekly))
		print("anatomie: {} hours weekly".format(anatomie.hours_weekly))
		print("wissenshaft: {} hours weekly".format(wissenshaft.hours_weekly))
		print("filosofie: {} hours weekly".format(filosofie.hours_weekly))
		print("")
		print("amount of work to get through celbio book: {} hours or {} hours weekly".format(celbio_book.hours_needed, round(celbio_book.hours_needed/semester_duration)))
		print("amount of work to get through all anatomy books: {} hours or {} hours weekly".format(anatomy_book.hours_needed, round(anatomy_book.hours_needed/semester_duration)))
		print("amount of work to get through philosophy book: {} hours or {} hours weekly".format(philosophy_book.hours_needed, round(philosophy_book.hours_needed/semester_duration)))
		print("amount of work to get through wissenshaft slides: {} hours or {} hours weekly".format(wissenshaft_slides.hours_needed, round(wissenshaft_slides.hours_needed/semester_duration)))
		

		print("---")
		print("weekly load = {} hours".format(round(weekly_load)))
		print("---")
		print("")
		apply_20_80("Celbio1 course weekly", celbio1.hours_weekly)
		apply_20_80("Celbio2 course weekly", celbio2.hours_weekly)
		apply_20_80("anatomy course weekly", anatomie.hours_weekly)
		apply_20_80("wissenshaft course weekly", wissenshaft.hours_weekly)
		apply_20_80("filosofie course weekly", filosofie.hours_weekly)
		print("")
		apply_20_80("celbio book",celbio_book.hours_needed/semester_duration)
		apply_20_80("anatomy book weekly",anatomy_book.hours_needed/semester_duration)
		print("---")
		apply_20_80("Weekly LOAD",weekly_load)
		print("---")

		important_reminder()
		print("")
		print("My study load (perfectionistic): {} hours, {} hours per week".format(weekly_load*semester_duration, weekly_load))
		print("My 20 - 80 study load: {} hours, {} hours per week".format(round(weekly_load*0.4*semester_duration), round(weekly_load*0.4)))
		print("Kuleuven recommended load: {} to {} hours, {} to {} hours per week".format(25*(11+9+4.5+4+3), 30*(11+9+4.5+4+3), round(25*(11+9+4.5+3)/semester_duration),round(30*(11+9+4.5+3)/semester_duration)))



main()