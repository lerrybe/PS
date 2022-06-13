def solution(participant, completion):
    participant.sort()
    completion.sort()

    while len(completion) != 0:
        m_participant = participant.pop()
        m_completion = completion.pop()
        if m_participant != m_completion: 
            return m_participant
            
    last_participant = participant.pop()
    return last_participant
