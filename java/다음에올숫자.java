int solution(int common[], size_t common_len) {
        int answer = 0;
        if((common[1] - common[0]) == (common[2] - common[1])){
            answer = common[common.length-1] + (common[1] - common[0]); // 등차수열
        } else {
            answer = common[common.length-1] * (common[1] / common[0]); // 등비수열
        }
        return answer;
}