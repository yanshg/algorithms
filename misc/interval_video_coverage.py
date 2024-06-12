
# get video clips which could cover all video length

# videos whose start <= curr_end could choose one last end one

def get_covered_video_clips(clips, end):
    if end == 0:
        return -1
    
    clips.sort(key = lambda x: (x[0], -x[1]))
    print(clips)
    
    i, n = 0, len(clips)
    res = 0
    curr_end = 0
    

    while i < n and clips[i][0] <= curr_end:
        # videos whose start <= curr_end could choose the one end lastly
        next_end = curr_end
        while i < n and clips[i][0] <= curr_end:
            next_end = max(next_end, clips[i][1])
            i += 1

        res += 1
        curr_end = next_end
        if curr_end >= end:
            return res

    return -1

clips = [[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]]
T = 10
print(get_covered_video_clips(clips, T))

clips = [[0,2],[4,6],[8,10],[1,5]]
T = 10
print(get_covered_video_clips(clips, T))
    

