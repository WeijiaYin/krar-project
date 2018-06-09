from typing import List

from structs.scenario import Scenario
import parsing.observation


def parse_file(file: str):
    with open(file) as f:
        lines = f.readlines()
    lines = [x.strip() for x in lines]
    observation_lines, action_occurrence_lines = split_scenario(lines)
    observations = parsing.observation.parse_all(observation_lines)

    return Scenario(observations, action_occurrence_lines)

def split_scenario(lines: List[str]):
    obs_idx = lines.index('OBS:')
    acs_idx = lines.index('ACS:')
    assert obs_idx < acs_idx
    observations = lines[obs_idx + 1:acs_idx]
    action_occurrences = lines[acs_idx + 1:]

    return (observations, action_occurrences)
