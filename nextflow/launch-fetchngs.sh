nextflow run nf-core/fetchngs \
	-profile docker,awsbatch \
	--awsqueue genomic-nextflow-queue \
	--awsregion us-east-1 \
	--input s3://genomic-nextflow/sample.csv \
	--outdir s3://genomic-nextflow/test/output/
	-work-dir s3://genomic-nextflow/test/ \
