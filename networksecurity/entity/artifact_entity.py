from dataclasses import dataclass


@dataclass
class DataIngestionArtifact:
    trainded_file_path:str
    test_file_path:str
    
    