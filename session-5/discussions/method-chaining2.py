from IPython import embed

class Source:
	def __init__(self):
		self.queries = []

	@classmethod
	def query(self, query_string):
		self.queries.append(query_string)

	def sort(self, sort="ASC"):
		self.sort = sort
		return self


	def perform(self):
		filters = ' && '.join(self.queries)
		row_sql_query = f'SELECT * FROM source WHERE {filters}'

		if self.sort:
			row_sql_query += f"SORT BY {self.sort}"

		print(row_sql_query)


def main():
	src = Source()
	src.query("FOOD == APPLE").query("COLOR == RED")

if __name__ == "__main__":
	main()