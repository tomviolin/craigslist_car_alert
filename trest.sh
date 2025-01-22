curl --url smtps://smtp.secureserver.net:485/ --mail-from 'tomviolin@spectrum.net' \
        --mail-rcpt 'tomviolin@spectrum.net' \
        -F "=testing body" \
        -H "Subject: subjecct/" \
	-H "From: tomviolin@spectrum.net" \
	-H "Content-Type: text/plain" \
	-H "Content-Transfer-Encoding: 7bit" \
	-H "MIME-Version: 1.0" \
	-H "Date: $(date -R)"
