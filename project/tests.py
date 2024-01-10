import os
import unittest
import subprocess

class TestDataPipeline(unittest.TestCase):

    def test_data_pipeline(self):
        
        try:
            subprocess.run(['bash', 'project/pipeline.sh'], check=True)
        except subprocess.CalledProcessError as e:
            self.fail(f"Data pipeline execution failed with error: {e}")

        output_file1 = 'data/crime_data.xlsx'
        output_file2 = 'data/population_density_data.xlsx'
        output_file3 = 'data/income_data.xlsx'

        self.assertTrue(os.path.exists(output_file1), f"{output_file1} does not exist")
        self.assertTrue(os.path.exists(output_file2), f"{output_file2} does not exist")
        self.assertTrue(os.path.exists(output_file3), f"{output_file3} does not exist")

if __name__ == '__main__':
    unittest.main()
