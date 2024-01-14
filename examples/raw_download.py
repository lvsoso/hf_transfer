from hf_transfer import raw_download


# url = "http://127.0.0.1:9000/test-1024/mp/76/4c/22e1eba33444dbb7dc58e98a87226c07fab484eeb5af1912fa0d09490fb0?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=TTZHZHDKQL26RNYRBN72%2F20240114%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240114T130519Z&X-Amz-Expires=604800&X-Amz-Security-Token=eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3NLZXkiOiJUVFpIWkhES1FMMjZSTllSQk43MiIsImV4cCI6MTcwNTI4MDY3NiwicGFyZW50IjoibWluaW9hZG1pbiJ9.hFb9MvQlT36kOeZs_uTDP4JHxuHfwui9blST8ps76f_VpTPxEBZpVLklpo_d6sLRfP3WC0eDaoMKp5UeX70z5w&X-Amz-SignedHeaders=host&versionId=null&X-Amz-Signature=2fd5542aa3fa1e2ccb5d7dd2e14cf34fe069e48c064c6df113a3c97b3f5fe06f"
url = "http://127.0.0.1:8282"
filename = "tmp-test-download-file"
max_files=5
chunk_size=10 * 1024 * 1024
parallel_failures=5
max_retries=5
headers={}
base_wait_time=5 * 1000
max_wait_time=10 * 1000
connect_timeout=10
request_timeout= 20

def callback(num):
    print(num)

if __name__ == '__main__':
    raw_download(
        url,
        filename,
        max_files,
        chunk_size,
        parallel_failures,
        max_retries,
        headers,
        base_wait_time,
        max_wait_time,
        connect_timeout,
        request_timeout,
        callback)